from django.urls import path, include

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path("", include("django.contrib.auth.urls")),
    path(r'<str:username>', views.profile, name='profile'),
    path('transfer/', views.transfer, name='transfer')
]