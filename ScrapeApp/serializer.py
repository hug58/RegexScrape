from rest_framework import serializers
from .models import PageExtract,RegexModel

class PageExtractSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageExtract
        fields = '__all__'


class PageExtractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageExtract
        exclude = ['data']

class RegexSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegexModel
        fields = '__all__'
