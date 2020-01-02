SHELL=/bin/sh
.SUFFIXES:
.SUFFIXES: .fut .py

srcdir=./clcell

./dist: ./build
	python3 setup.py bdist_wheel --skip-build

./build: $(srcdir)/device_api.py
	python3 setup.py build

$(srcdir)/device_api.py: $(srcdir)/device_api.fut
	futhark pyopencl --library $(srcdir)/device_api.fut

.PHONY: clean
clean:
	rm -rf $(srcdir)/device_api.py ./dist ./build ./*.egg-info $(srcdir)/__pycache__ ./.eggs

.PHONY: install
install: ./build
	python3 setup.py install --skip-build --user
