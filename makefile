

run-task:
	celery -A regex_scrape worker -l INFO

run:
	python manage.py runserver