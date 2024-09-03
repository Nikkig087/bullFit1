from django.urls import path
from . import views
from .views import contact_form, report_comment
from .views import ExerciseListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.ExerciseListView.as_view(), name="home"),
    path("exercise/<int:pk>/", views.exercise_detail, name="exercise_detail"),
    path(
        "exercise/<int:pk>/comment/edit/<int:comment_id>/",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "exercise/<int:pk>/comment/delete/<int:comment_id>/",
        views.delete_comment,
        name="delete_comment",
    ),
    path(
        "exercise/<int:pk>/add_comment/", views.add_comment, name="add_comment"
    ),
    path(
        "contact/", contact_form, name="contact_form"
    ),  # For function-based view
    path(
        "report_comment/<int:comment_id>/",
        views.report_comment,
        name="report_comment",
    ),
     path(
        'accounts/login/', auth_views.LoginView.as_view(), name='login')
]
