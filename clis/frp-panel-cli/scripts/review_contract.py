"""Rebuild the HTTP contract from the pinned frp-panel source, without running it."""
import json,re,subprocess
from pathlib import Path
import sys
src=Path(sys.argv[1]).resolve(); root=Path(__file__).resolve().parents[1]
pinned='1a58b856d7de19de8669b7072872986d2fa1604a'
assert subprocess.check_output(['git','-C',str(src),'rev-parse','HEAD'],text=True).strip()==pinned, 'Review required for new upstream revision'
assert not subprocess.check_output(['git','-C',str(src),'status','--porcelain'],text=True).strip(), 'Review requires clean upstream'
raw='\n'.join(p.read_text() for p in sorted((src/'pb').glob('*.pb.go')))
structs=dict(re.findall(r'type (\w+) struct \{(.*?)\n\}',raw,re.S))
enums=set(re.findall(r'type (\w+) int32',raw))
schemas={}
def field_schema(t):
 t=t.lstrip('*')
 if t=='[]byte': return {'type':'string','format':'byte'}
 if t.startswith('[]'): return {'type':'array','items':field_schema(t[2:])}
 if t.startswith('map['):
  m=re.fullmatch(r'map\[([^]]+)\](.+)',t); assert m,t
  return {'type':'object','additionalProperties':field_schema(m[2])}
 if t in ('string','bool'): return {'type':{'bool':'boolean'}.get(t,t)}
 if t in ('float32','float64'): return {'type':'number'}
 if re.fullmatch(r'u?int(32|64)',t) or t in enums: return {'type':'integer'}
 assert t in structs,t
 make_schema(t)
 return {'$ref':'#/components/schemas/'+t}
def make_schema(name):
 if name in schemas:return
 schemas[name]={'type':'object','properties':{}}
 for line in structs[name].splitlines():
  m=re.search(r'^\s*\w+\s+(\S+)\s+`.*?json:"([^",]+)',line)
  if m and m[2]!='-': schemas[name]['properties'][m[2]]=field_schema(m[1])
groups={'router':''}; paths={}; provenance=[]; excluded=[]
imports={'wgHandler':'wg'}
handlertext={p.name:'\n'.join(f.read_text() for f in sorted(p.glob('*.go'))) for p in (src/'biz/master').iterdir() if p.is_dir()}
for n,line in enumerate((src/'biz/master/handler.go').read_text().splitlines(),1):
 g=re.search(r'(\w+) := (\w+)\.Group\("([^"]+)"',line)
 if g:
  assert g[2] in groups; groups[g[1]]=groups[g[2]]+g[3]
 m=re.search(r'(\w+)\.(GET|POST)\("([^"]+)"',line)
 if not m:continue
 path=groups[m[1]]+m[3]; method=m[2].lower()
 if path in ('/auth','/api/v1/auth/logout','/api/v1/pty/:clientID','/api/v1/log'):
  excluded.append({'path':path,'reason':'plugin callback, cookie logout, or WebSocket protocol'});continue
 h=re.search(r'app.Wrapper\(appInstance, (\w+)\.(\w+)\)',line)
 req=None
 if h:
  content=handlertext[imports.get(h[1],h[1])]
  sig=re.search(r'func '+h[2]+r'\([^)]*\*pb\.(\w+)\)\s*\(\*pb\.(\w+),\s*error\)',content)
  assert sig,(path,h[2]);req,resp=sig.groups()
 else:
  assert path=='/api/v1/platform/baseinfo',path;resp='GetPlatformInfoResponse'
 make_schema(resp)
 parts=path.removeprefix('/api/v1/').split('/')
 op={'operationId':'_'.join(parts).replace('-','_'),'tags':[parts[0]],'summary':' '.join(parts),
     'security':[] if parts[0]=='auth' else [{'bearerAuth':[]}],
     'responses':{'200':{'description':'frp-panel envelope; code 200 means success, even though errors also use HTTP 200', 'content':{'application/json':{'schema':{'type':'object','properties':{'code':{'type':'integer'},'msg':{'type':'string'},'body':{'$ref':'#/components/schemas/'+resp}}}}}}}}
 if req:
  make_schema(req);op['requestBody']={'required':True,'content':{'application/json':{'schema':{'$ref':'#/components/schemas/'+req}}}}
 assert method not in paths.get(path,{})
 paths.setdefault(path,{})[method]=op;provenance.append({'method':method,'path':path,'request':req,'response':resp,'source':f'biz/master/handler.go:{n}'})
out=root/'specs';out.mkdir(exist_ok=True)
contract={'openapi':'3.0.3','info':{'title':'frp-panel HTTP API','version':pinned},'paths':paths,'components':{'securitySchemes':{'bearerAuth':{'type':'http','scheme':'bearer','bearerFormat':'JWT'}},'schemas':schemas}}
(out/'openapi.json').write_text(json.dumps(contract,indent=2)+'\n')
(out/'sources.yaml').write_text('sources:\n  panel:\n    local_path: .\n    backend: openapi3\n    openapi3:\n      files: [openapi.json]\n')
(out/'review.json').write_text(json.dumps({'commit':pinned,'operations':provenance,'excluded':excluded},indent=2)+'\n')
print(f'Reviewed {len(provenance)} operations, {len(schemas)} schemas; excluded {len(excluded)} nonstandard endpoints')
