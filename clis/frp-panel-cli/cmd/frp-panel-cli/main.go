package main
import (
 _ "embed"
 "os"
 "github.com/lathe-cli/lathe/pkg/lathe"
 "local/frp-panel-cli/internal/generated"
)
//go:embed cli.yaml
var manifest []byte
func main() { os.Exit(lathe.Run(lathe.RunOptions{Manifest: manifest, Mount: generated.Mount})) }
