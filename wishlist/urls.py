from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.logreg.urls', namespace='logreg')),
    url(r'^', include('apps.lists.urls', namespace='lists')),
]
