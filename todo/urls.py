from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
#from .views import CreatePostView

urlpatterns = [
	path('', views.index, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
	path('deleteall', views.deleteall, name='deleteall'),
	path('deletecomplete', views.deletecompleted, name='deletecomplete'),
	path('complete/<todo_id>', views.completeTodo, name='complete'),
	#path('post/<int:pk>/note/', views.add_note_to_post, name='add_note_to_post'),
	#path('post/', CreatePostView.as_view(), name='add_post'),
	#path('posts/', views.post_list, name='post_list'),
	#path('posts/<int:pk>/', views.delete_post, name='delete_post'),
	path('updatenotiz/<str:pk>/', views.updatenotiz, name="updatenotiz"),
	path('searchdata', views.searchdata, name='searchdata'),




]

