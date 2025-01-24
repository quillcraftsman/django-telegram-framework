test:
	python manage.py test

coverage:
	coverage run --source='.' manage.py test
	coverage html
	coverage report --fail-under=100

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
	pip uninstall django-telegram-framework -y
	rm -rf dist
	rm -rf telegram-framework.egg-info

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
	sphinx-apidoc -o docs/package telegram_framework/

run_bot:
	python manage.py run_bot --settings=settings.prod_settings

run_demo_bot:
	python manage.py run_bot --bot_links=demo.links --settings=settings.prod_settings

run_quickstart_bot:
	python manage.py run_bot --bot_links=quickstart.bot --settings=settings.prod_settings

server:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate