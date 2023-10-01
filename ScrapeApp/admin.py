from django.contrib import admin

# Register your models here.
from .models import PageExtract, RegexModel

admin.site.register(PageExtract)
admin.site.register(RegexModel)