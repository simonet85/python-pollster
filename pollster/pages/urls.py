from django.urls import path

from . import views

#routing
urlpatterns = [
    path('',views.index, name='index'),
]