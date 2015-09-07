SRCDIR  := .
FILES := $(shell find $(SRCDIR) -not -path venv -type f -name "*.py")

test:
	nosetests --with-doctest $(FILES)
