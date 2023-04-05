from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post

# Urls for blog pages 
# Insert blog app urls patterns here
urlpatterns = [
    path('', ListView.as_view(
            queryset=
            Post.objects.all().order_by("-date")[:25],
            template_name="events.html"
            )
         ),
    path('<int:pk>/', DetailView.as_view(
            model=Post,
            template_name="quotes.html"
            )
         ),
]