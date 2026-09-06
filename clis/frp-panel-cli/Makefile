.PHONY: generate build test

generate:
	lathe bootstrap
	cp cli.yaml cmd/frp-panel-cli/cli.yaml

build:
	go build -trimpath -o bin/frp-panel-cli ./cmd/frp-panel-cli

test:
	python3 scripts/smoke.py
