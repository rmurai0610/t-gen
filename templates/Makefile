all:
	mkdir -p build; \
	cd build;       \
	cmake ..;       \
	make -j;        \
	cd ..;          \

ifeq (test,$(firstword $(MAKECMDGOALS)))
  TEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(TEST_ARGS):;@:)
endif

test:
	./test.py $(TEST_ARGS)

clean:
	cd build && make clean && cd ..

.PHONY: test clean $(TEST_ARGS)
