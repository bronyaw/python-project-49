#Makefile~
install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry builds

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*whl

linter-check:
	poetry run flake8 brain_games
