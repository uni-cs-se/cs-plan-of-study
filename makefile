
gen: gen.py clean
	mkdir build; \
	cd build; \
	python ../$< .

run: gen
	./run.sh

clean:
	rm -rf build

.PHONY: clean gen run
