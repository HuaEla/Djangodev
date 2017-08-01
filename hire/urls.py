from . import views
from django.conf.urls import url



urlpatterns=[
    url(r'^hire',views.hires,name='hire'),
]
