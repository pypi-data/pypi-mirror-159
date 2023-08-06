.PHONY: install_deps format lint test test_with_coverage report_coverage coverage tox push publish

install_deps:  ## Install dependencies
	python -m pip install --upgrade pip
	python -m pip install black mccabe flake8 flit pyflakes mypy pylint \
	                      hypothesis pytest coverage tox tox-gh-actions 

format:  ## Format code
	python -m black calculator
	python -m black tests

lint:  ## Lint and static-check
	python -m flake8 calculator
	python -m pyflakes -V calculator
	python -m mypy calculator
	python -m pylint --verbose calculator

test:  ## Run tests
	python -m pytest -ra --doctest-modules --doctest-continue-on-failure


test_with_coverage:  ## Run tests with coverage
	python -m coverage erase
	python -m coverage run --include=calculator/* -m pytest -ra \
	                       --doctest-modules --doctest-continue-on-failure

report_coverage:  ## Report coverage, if test with coverage were already run
	python -m coverage report -m
	python -m coverage xml

coverage:  ## Run tests and report coverage
	make test_with_coverage
	make report_coverage

tox:   ## Run tox
	python -m tox

push:  ## Push code with tags
	git push && git push --tags

publish:  ## Publish to PyPi
	python -m flit publish

