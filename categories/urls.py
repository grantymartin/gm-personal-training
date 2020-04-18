from django.conf.urls import url
from .views import do_categories

urlpatterns = [
    url(r'^$', do_categories, name='categories')
]