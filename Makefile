# Makefile for Severino
TARGET_DIR=screenshots

default: help

### tests
tests-unit:
	nosetests test/unit/*.py

tests-external:
	nosetests test/external/*.py

tests-pyccuracy:
	cd test/pyccuracy; pyccuracy_console -P pages -e webdriver -A actions

tests:
	make tests-unit
	make tests-external

### env
dependencies:
	@echo "Installing dependencies..."
	@curl -L -o virtualenv.py https://raw.github.com/pypa/virtualenv/master/virtualenv.py
	@python virtualenv.py severino-venv
	@. severino-venv/bin/activate; pip install -r requirements.txt
	@echo "Done."

clean:
	@echo "Removing the virtualenv files"
	@rm -rf severino-venv
	@echo "Done."


### app
capture:
	@echo "taking screenshots into ./$(TARGET_DIR)/"
	@echo "not implemented yet ;P"

## help
help:
	@echo "dependencies:\t install the development dependencies"
	@echo "clean:\t\t removes the virtualenv"
	@echo "\t\t"
	@echo "tests:\t run all tests"
	@echo "tests-unit:\t run all unit tests"
	@echo "tests-external:\t run all external tests"
