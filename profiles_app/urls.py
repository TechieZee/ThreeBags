from django.urls import path
from . import views
app_name = 'profiles_app'

urlpatterns = [
	
	path('new_stream/', views.new_stream, name='new_stream'),
	path('new_college/', views.new_college, name='new_college'),

]