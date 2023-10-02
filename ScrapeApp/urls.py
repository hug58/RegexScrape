from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PageExtractViewSet, RegexViewSet

ROUTER = DefaultRouter()
ROUTER.register(r'page', PageExtractViewSet)
ROUTER.register(r'regex', RegexViewSet)


urlpatterns = [
    path('', include(ROUTER.urls)),
]

