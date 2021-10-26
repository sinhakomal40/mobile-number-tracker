from django.conf.urls import url, include
from tracker.views import *

urlpatterns = [
    url(r'^$', home),
]
