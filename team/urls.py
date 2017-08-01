from . import views
from django.conf.urls import url



urlpatterns=[
    url(r'^team',views.team,name='team'),
]
