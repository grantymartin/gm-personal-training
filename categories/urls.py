from django.conf.urls import url
from .views import CategoryForm

urlpatterns = [
    url(r'^$', CategoryForm, name='categories')
]