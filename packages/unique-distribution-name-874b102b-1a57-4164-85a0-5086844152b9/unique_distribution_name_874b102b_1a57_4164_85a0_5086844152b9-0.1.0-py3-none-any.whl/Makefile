# Makefile

DIST_DIR=dist/
VIRTUALENV_DIR=venv/

DOCS_SITE=docs/site/
DOCS_SRC_FILES=$(shell find ./docs -type f ! -path './$(DOCS_SITE)*')
PYTHON_SRC_DIR=src/
PYTHON_SRC_FILES=$(shell find ./src -type f -path './$(PYTHON_SRC_DIR)*.py')

# will have the name of the sdist/bdist if they exist, and so won't build, else won't and will build
SDIST=$(shell printf $(DIST_DIR)*.tar.gz)
BDIST=$(shell printf $(DIST_DIR)*.whl)

all: build-docs-site build-dist dry-run-publish
re: fclean all

# run all defined tests for python distribution
test:
	poetry install pytest
	poetry run pytest

# build only "source distribution" (sdist)
sdist: build-sdist
build-sdist: $(SDIST)
$(SDIST):
	poetry build --format sdist
# rebuild only "source distribution" (sdist)
resdist: rebuild-sdist
rebuild-sdist: clean-sdist build-sdist
# show contents of sdist
show-sdist: build-sdist
	@echo 'Source Distribution (SDIST):'
	@tar --verbose --list --file $(DIST_DIR)*.tar.gz
	@echo

# build only "build distribution" (bdist)
bdist: build-bdist
build-bdist: $(BDIST)
wheel: build-wheel
build-wheel: $(BDIST)
$(BDIST):
	poetry build --format wheel
# rebuild only "build distribution" (bdist)
rebdist: rebuild-bdist
rebuild-bdist: clean-bdist build-bdist
# show contents of bdist
show-bdist: build-bdist
	@echo 'Build Distribution (BDIST/wheel):'
	@tar --verbose --list --file $(DIST_DIR)*.whl
	@echo

# build both sdist and bdist
build: build-dist
dist: build-dist
build-dist: build-sdist build-bdist
# rebuild both sdist and bdist
rebuild: rebuild-dist
redist: rebuild-dist
rebuild-dist: clean-dist build-dist
# show contents of both distributions
show: show-dist
show-all: show-dist
show-dist: build-dist show-sdist show-bdist

# launch web server hosting documentation site
serve: serve-docs
serve-docs:
	(poetry run sh -c 'cd docs/ && mkdocs serve')

# build the documentation site in the local directory defined in ./docs/mkdocs.yaml in the field `site`
site: build-docs-site
docs: build-docs-site
build-docs-site: $(DOCS_SITE)
$(DOCS_SITE): $(DOCS_SRC_FILES)
	(poetry run sh -c 'cd docs/ && mkdocs build')

# dry-run publish distribution to PyPI
dry-run-publish: re
	poetry publish --dry-run

# publish distribution to PyPI
publish: re
	poetry publish

# clean sdist, bdist, and both distributions
clean-sdist:
	rm -rf ./dist/*.tar.gz
clean-bdist:
	rm -rf ./dist/*.whl
clean: clean-dist
clean-dist:
	rm -rf ./dist/

# clean dist. and environments
fclean: clean-dist
	rm -rf ./.venv/
	rm -rf ./docs/site/

.PHONY: all re sdist build-sdist resdist rebuild-sdist show-sdist bdist build-bdist wheel build-wheel rebdist rebuild-bdist show-bdist build dist build-dist rebuild redist rebuild-dist show show-all show-dist serve site docs build-docs-site dry-run-publish publish clean fclean
