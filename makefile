.PHONY: run
run: black
	python3 src/main.py

.PHONY: black
black:
	python3 -m black src
