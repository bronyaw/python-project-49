install:
	poetry install

brain-games:
	poetry run brain-games
	poetry run brain-even
	poetry run brain-calc
	poetry run brain-gcd
	poetry run brain-progression
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*whl

make-lint:
	poetry run flake8 brain_games
	poetry run flake8 brain_even
	poetry run flake8 brain_calc
	poetry run flake8 brain_gcd
	poetry run flake8 brain_progression
	poetry run flake8 brain_prime