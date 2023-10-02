"""config"""
from django.apps import AppConfig

class ScrapeappConfig(AppConfig):
    """Scrape app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scrape_app'
