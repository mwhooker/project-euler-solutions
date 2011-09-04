SRCDIR  := .
FILES := $(shell find $(SRCDIR) -type f -name "*.py")

test:
	nosetests --with-doctest $(FILES)
