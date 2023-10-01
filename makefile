

run-task:
	celery -A RegexScrape worker -l INFO

run:
	python manage.py runserver