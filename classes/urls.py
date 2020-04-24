from django.conf.urls import url, include
from classes.views import  email

urlpatterns = [
    url(r'^classes/', email, name="classes"),
]