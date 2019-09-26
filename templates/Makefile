all:
	mkdir -p build; \
	cd build;       \
	cmake ..;       \
	make -j;        \
	cd ..;          \

test:
	./test.py

clean:
	cd build && make clean && cd ..

.PHONY: test clean
