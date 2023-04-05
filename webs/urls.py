from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('contact_us/', views.contact),
]
