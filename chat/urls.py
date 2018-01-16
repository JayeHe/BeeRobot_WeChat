# _*_coding:utf-8_*_
# Author:Jaye He

from django.conf.urls import url
from chat import views

urlpatterns = [
    url(r'^$', views.home),
]