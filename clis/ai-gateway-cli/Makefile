.PHONY: generate build test skill-install-dry skill-install

generate:
	lathe bootstrap
	cp cli.yaml cmd/ai-gateway-cli/cli.yaml

build:
	go build -trimpath -o bin/ai-gateway-cli ./cmd/ai-gateway-cli

test:
	python3 scripts/smoke.py

skill-install-dry:
	go run ./cmd/kitup-install

skill-install:
	go run ./cmd/kitup-install --apply
