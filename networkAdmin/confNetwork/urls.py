__author__ = 'karon'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<datacenter_id>[0-9]+)/$', views.index, name="index_dc")
]