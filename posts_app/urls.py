from django.urls import path, include
from . import views

app_name = 'posts_app'

urlpatterns = [
	path('<int:post_id>/', views.post_detail, name='post_detail'),
	path('create/', views.post_create, name='post_create'),
	path('', views.posts_list, name='posts_list'),
	path('send_to_all/<int:post_id>', views.send_to_all, name='send_to_all'),
]