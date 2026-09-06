.PHONY: build test
build:
	$(MAKE) -C clis/frp-panel-cli build

test:
	$(MAKE) -C clis/frp-panel-cli test
