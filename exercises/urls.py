from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='home'),
    path('exercises/', views.ExerciseListView.as_view(), name='exercise_list'),
    path('exercise/<int:pk>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercise/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('exercise/<int:pk>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('exercise/<int:pk>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    
]
