""" Register your models here. """
from django.contrib import admin

from .models import PageExtract, RegexModel

admin.site.register(PageExtract)
admin.site.register(RegexModel)
