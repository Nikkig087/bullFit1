from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ExerciseDetailView, edit_comment, delete_comment

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='home'),
    path('exercises/', views.ExerciseListView.as_view(), name='exercise_list'),
    path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercise/<int:pk>/comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('exercise/<int:pk>/comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('exercise/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    
]
