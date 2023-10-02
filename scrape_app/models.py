"""models"""
from django.db import models


class RegexModel(models.Model):
    """Model that represents a regular expression"""
    name = models.CharField(max_length=250)
    pattern = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        """Base class for objects"""
        ordering = ['-created_at']


    def __str__(self):
        return f'This regex matches {self.name}'

class PageExtract(models.Model):
    """Model for extracting pages from"""
    data = models.JSONField(blank=True, null=True)
    regex = models.ManyToManyField(RegexModel)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    var_url_paginate = models.CharField(blank=True,max_length=250)
    path_paginate = models.CharField(blank=True, max_length=250)
    url_base = models.CharField(max_length=250)
    is_paginational = models.BooleanField(default=False)


    class Meta:
        """Base class for objects"""
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.regex} : {self.url_base}'
