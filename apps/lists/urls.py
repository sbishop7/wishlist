from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.index, name='index'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^wish_items/create$', views.create, name='create'),
    url(r'^wish_items/(?P<id>\d+)$', views.wish_items, name='wish_items'),
    url(r'^add_product$', views.add_product, name='add_product'),
    url(r'^delete_product/(?P<id>\d+)$', views.delete_product, name='delete_product'),
    url(r'^add_wish/(?P<id>\d+)$', views.add_wish, name='add_wish'),
    url(r'^remove_wish/(?P<id>\d+)$', views.remove_wish, name='remove_wish')
]
