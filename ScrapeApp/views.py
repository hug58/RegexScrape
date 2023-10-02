
import json

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .models import PageExtract,RegexModel
from .serializer import PageExtractSerializer, RegexSerializer, PageExtractListSerializer
from rest_framework import status
from django.http import Http404



from .tasks import get_pages_and_process_with_regex
    
class PageExtractViewSet(viewsets.ModelViewSet):
    queryset= PageExtract.objects.all()
    serializer_class = PageExtractSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return PageExtractListSerializer
        return super().get_serializer_class()

    def create(self, request, format=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        page = serializer.save()
        get_pages_and_process_with_regex.delay(serializer.data,page.id)
        return Response(serializer.data, status=202)
    
class RegexViewSet(viewsets.ModelViewSet):
    queryset = RegexModel.objects.all()
    serializer_class = RegexSerializer  