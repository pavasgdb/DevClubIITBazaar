from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('register/', user_views.register, name='register'),
	path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin'),
	path('signout/', auth_views.LogoutView.as_view(template_name='users/signout.html'), name='signout'),
]
