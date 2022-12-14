from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('profile/', views.profile, name='profile'),
    path('transfer/', views.transfer, name='transfer'),
    path('', TemplateView.as_view(template_name='registration/home.html'), name='home'),
]