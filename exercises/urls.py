from django.urls import path
from . import views
from .views import contact_view, thank_you_view

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='home'),
    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercise/<int:pk>/comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('exercise/<int:pk>/comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('exercise/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('contact/', contact_view, name='contact'),  # For function-based view
    path('thank-you/', thank_you_view, name='thank_you'), 
]
