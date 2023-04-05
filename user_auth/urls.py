from django.urls import path
from .import views

# Here we set up urls for authentication.
# Adding urls for user authentication here
app_name = 'user_auth'
urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('show_user/', views.show_user, name='show_user')
]
