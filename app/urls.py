from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'<str:username>', views.homePage, name='home')
]