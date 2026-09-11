.PHONY: build test
build:
	$(MAKE) -C clis/frp-panel-cli build
	$(MAKE) -C clis/ai-gateway-cli build

test:
	$(MAKE) -C clis/frp-panel-cli test
	$(MAKE) -C clis/ai-gateway-cli test
