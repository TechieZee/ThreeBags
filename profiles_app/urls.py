from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views
app_name = 'profiles_app'

urlpatterns = [
	path('', views.managers_home, name='managers_home'),
	path('new_stream/', views.new_stream, name='new_stream'),
	path('new_college/', views.new_college, name='new_college'),
	path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

]