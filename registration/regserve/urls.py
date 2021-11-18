from django.urls import path

from . import views

applications = 'regserve'

urlpatterns = [
    path('', views.index, name='index')
]

