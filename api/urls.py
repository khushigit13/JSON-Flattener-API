from django.urls import path
from .views import JsonFlattenerViewSet

urlpatterns = [
    path('jsonFlattener/', JsonFlattenerViewSet.as_view(), name='flatten-json'),
]
