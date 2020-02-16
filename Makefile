
update:
	pip-compile -o requirements.txt

setup:
	pip install -r requirements.txt
	pip install coverage pip-tools
	npm install
	python manage.py migrate
	python populate.py
	python manage.py createsuperuser

test:
	coverage run manage.py test
	coverage report
