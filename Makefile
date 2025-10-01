export PYTHONPATH := plugins/mkdocs-uktre-glossary-plugin/src:$(PYTHONPATH)

# https://lychee.cli.rs/usage/cli/
LYCHEE_ARGS := --no-progress --include-fragments --index-files index.html --root-dir $(PWD)/site/ site/index.html

pre-build:
	python ./plugins/create_category_pages.py

build: pre-build
	mkdocs build --strict

serve: pre-build
	mkdocs serve

# https://lychee.cli.rs/
# https://github.com/lycheeverse/lychee/releases/tag/lychee-v0.20.1
linkcheck-internal:
	lychee --offline $(LYCHEE_ARGS)

# Use caching for the full check to reduce likelihood of hitting rate limits
# See .lycheeignore for ignored URLs
linkcheck:
	lychee --cache $(LYCHEE_ARGS)

.PHONY: clean
clean:
	rm -f docs/categories/*
	rm -rf site/*
