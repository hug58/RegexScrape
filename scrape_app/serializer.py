"""serializers"""
from rest_framework import serializers
from .models import PageExtract,RegexModel

class PageExtractSerializer(serializers.ModelSerializer):
    """Serializer for PageExtract, use for detail"""
    class Meta:
        """Meta serializer for PageExtract"""
        model = PageExtract
        fields = '__all__'


class PageExtractListSerializer(serializers.ModelSerializer):
    """Serializer for PageExtractList, list and create"""
    class Meta:
        """Meta serializer for PageExtractList"""
        model = PageExtract
        exclude = ['data']

class RegexSerializer(serializers.ModelSerializer):
    """RegexSerializer for Regex"""
    class Meta:
        """Meta serializer for Regex"""
        model = RegexModel
        fields = '__all__'
