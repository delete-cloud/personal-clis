"""Exercise generated commands against loopback only, using synthetic credentials."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json,os,subprocess,tempfile,threading
root=Path(__file__).resolve().parents[1]; binary=root/'bin/frp-panel-cli'
calls=[]; response={'code':200,'msg':'success','body':{'clients':[]}}
class Handler(BaseHTTPRequestHandler):
 def log_message(self,*args):pass
 def do_GET(self):self.reply()
 def do_POST(self):self.reply()
 def reply(self):
  body=self.rfile.read(int(self.headers.get('Content-Length',0)))
  calls.append((self.command,self.path,self.headers.get('Authorization'),json.loads(body) if body else None))
  data=json.dumps(response).encode();self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
 with tempfile.TemporaryDirectory(prefix='frp-cli-test-') as tmp:
  env=dict(os.environ,FRP_PANEL_CLI_CONFIG_DIR=tmp,FRP_PANEL_HOST=f'http://127.0.0.1:{server.server_port}')
  def run(*args,stdin=None):
   p=subprocess.run([str(binary),*args],input=stdin,text=True,capture_output=True,env=env,timeout=10)
   assert p.returncode==0,(args,p.stderr);return json.loads(p.stdout) if p.stdout.strip().startswith('{') else p.stdout
  assert run('__lathe','verify','--json')['ok']
  catalog=run('commands','--json')['commands']; assert len(catalog)==65
  run('auth','login','--hostname',env['FRP_PANEL_HOST'],'--with-token','--skip-validate',stdin='synthetic-test-token\n');assert not calls
  empty=Path(tmp)/'empty.json';empty.write_text('{}')
  review=json.loads((root/'specs/review.json').read_text());expected={(x['method'].upper(),x['path']) for x in review['operations']}
  actual=set()
  for item in catalog:
   args=item['path'];body=['--file',str(empty)] if item.get('body') else []
   before=len(calls); preview=run(*args,*body,'--dry-run')
   assert len(calls)==before,'dry run sent traffic'
   assert preview['url']==env['FRP_PANEL_HOST']+item['http']['path_template']
   assert run(*args,*body,'-o','json')==response
   method,path,auth,payload=calls[-1];actual.add((method,path))
   assert method==item['http']['method'] and path==item['http']['path_template']
   if item['auth']['required']:assert auth=='Bearer synthetic-test-token'
   assert payload==({} if body else None)
  assert actual==expected
  run('panel','client','list','--set','page=2','--set','page_size=10','--set-str','keyword=example','-o','json')
  assert calls[-1][3]=={'page':2,'page_size':10,'keyword':'example'}
  response={'code':500,'msg':'synthetic application error'}
  assert run('panel','client','list','--file',str(empty),'-o','json')==response
  print('PASS: 65 catalog contracts, 65 network-free previews, 65 loopback HTTP requests, Bearer auth, typed JSON body, and HTTP-200 error-envelope preservation')
finally:server.shutdown();server.server_close();thread.join()
