from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercise/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('exercise/<int:pk>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('exercise/<int:pk>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
