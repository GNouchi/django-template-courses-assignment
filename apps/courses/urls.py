from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^deletecourse/(?P<id>\d+)$', views.deletecourse),
    url(r'^', views.index),
]