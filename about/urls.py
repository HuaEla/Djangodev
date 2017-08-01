from . import views
from django.conf.urls import url



urlpatterns=[
    url(r'^about',views.messageview,name='about'),
]
