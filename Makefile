test:
	python manage.py test

coverage:
	coverage run --source='.' manage.py test
	coverage html --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py,package.py,*/management/*
	coverage report --omit=settings/asgi.py,settings/wsgi.py,manage.py,setup.py,package.py,*/management/* --fail-under=100

yamllint:
	yamllint -d relaxed .

black:
	black .

build:
	python -m build

install:
	make build
	pip install dist/*.whl

uninstall:
	pip uninstall pygenesis -y
	rm -rf dist
	rm -rf pygenesis_django.egg-info

reinstall:
	make uninstall
	make install

pylint:
	pylint $(shell git ls-files '*.py')

lint:
	make yamllint
	make pylint

sphinx-help:
	make help -f Sphinxfile

package_docs:
	sphinx-apidoc -o docs/package pygenesis_django/