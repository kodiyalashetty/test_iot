
all:
	python setup.py build
	ln -sf `find ./ -name "_openhpi.so" | head -n1`

install:
	python setup.py install --prefix=/usr

dist:
	python setup.py sdist

clean:
	rm -rf build dist *_wrap.c openhpi.py *.pyc MANIFEST *.so

