from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ExerciseListView, exercise_detail,edit_comment

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='home'),
   # path('exercises/', views.ExerciseListView.as_view(), name='exercise_list'),
    #path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
    path('', ExerciseListView.as_view(), name='exercise_list'),
    path('exercise/<int:pk>/', exercise_detail, name='exercise_detail'),
    path('exercise/<int:pk>/comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('exercise/<int:pk>/comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('exercise/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    
]
