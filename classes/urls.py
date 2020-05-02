from django.conf.urls import url
from .views import  email

urlpatterns = [
    url(r'^$', email, name="classes"),
]