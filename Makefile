# Makefile for Severino

default: help

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

help:
	@echo "dependencies:\t install the development dependencies"
	@echo "clean:\t\t removes the virtualenv"
