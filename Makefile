
pre-build:
	python ./plugins/create_category_pages.py

build: pre-build
	mkdocs build --strict

serve: pre-build
	mkdocs serve

.PHONY: clean
clean:
	rm -f docs/categories/*
	rm -rf site/*
