# -- coding: utf-8 --

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^complete/$', views.complete, name='complete'),
]
