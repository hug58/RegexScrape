
from rest_framework.response import Response
from rest_framework import viewsets

from .models import PageExtract,RegexModel
from .serializer import PageExtractSerializer, RegexSerializer, PageExtractListSerializer
from .tasks import get_pages_and_process_with_regex

    
class PageExtractViewSet(viewsets.ModelViewSet):
    """View set to extract"""
    queryset= PageExtract.objects.all()
    serializer_class = PageExtractSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return PageExtractListSerializer
        return super().get_serializer_class()

    def create(self, request, format=None, *args, **kwargs):
        """Create a new page extract and download page html and extract data with regex"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        page = serializer.save()
        get_pages_and_process_with_regex.delay(serializer.data,page.id)
        return Response(serializer.data, status=202)
    
class RegexViewSet(viewsets.ModelViewSet):
    """ Viewset regex"""
    queryset = RegexModel.objects.all()
    serializer_class = RegexSerializer
