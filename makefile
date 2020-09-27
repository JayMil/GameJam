.PHONY: run
run: black
	python3 src/main.py

.PHONY: black
black:
	python3 -m black src

.PHONY: install_deps
install_deps:
	 pip3 install -r requirements.txt
	 pre-commit install
