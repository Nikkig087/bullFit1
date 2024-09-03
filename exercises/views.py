from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Exercise, Comment, CommentReport
from .forms import CommentForm
from django.views import generic
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactMessageForm, ReportCommentForm
from django.db import models
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ExerciseListView(generic.ListView):
    model = Exercise
    template_name = "exercises/exercise_list.html"
    context_object_name = "exercises"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_form"] = (
            ContactMessageForm()
        )  # Use 'contact_form' to avoid confusion
        return context

    def get_queryset(self):
        return Exercise.objects.order_by("title")  # Ordered by title


def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    comments = exercise.comments.all()
    comment_form = CommentForm()
    comment_count = comments.count()

    context = {
        "exercise": exercise,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }

    return render(request, "exercises/exercise_detail.html", context)


@login_required
def edit_comment(request, pk, comment_id):
    exercise = get_object_or_404(Exercise, pk=pk)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("exercise_detail", pk=exercise.pk)
    else:
        form = CommentForm(instance=comment)
    return render(
        request,
        "exercises/edit_comment.html",
        {
            "exercise": exercise,
            "comment": comment,
            "form": form,
        },
    )


@login_required
def add_comment(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.exercise = exercise
            comment.user = request.user
            comment.save()
            messages.success(
                request,
                "Your comment has been added and is awaiting approval.",
            )
            return redirect("exercise_detail", pk=exercise.pk)
    else:
        form = CommentForm()
    return render(
        request,
        "exercises/add_comment.html",
        {"form": form, "exercise": exercise},
    )


@login_required
def delete_comment(request, pk, comment_id):
    exercise = get_object_or_404(Exercise, pk=pk)
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )
    return redirect("exercise_detail", pk=pk)


def contact_form(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message. We will get back to you soon!')
            return redirect('home')  # Redirect to a success page or back to the home page
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = ContactMessageForm()

    return render(request, 'exercises/contact_form.html', {'form': form})

def report_comment(request, comment_id):
    # Check if the user is authenticated immediately
    if not request.user.is_authenticated:
        # If it's an AJAX request, return a JSON response with a redirect URL
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"redirect_url": "/accounts/login/"}, status=403)
        # Otherwise, redirect to the login page
        return redirect("login")

    # Fetch the comment and associated exercise
    comment = get_object_or_404(Comment, id=comment_id)
    exercise = comment.exercise  # Assuming Comment has a ForeignKey to Exercise

    if request.method == 'POST':
        form = ReportCommentForm(request.POST)
        if form.is_valid():
            CommentReport.objects.create(
                user=request.user,
                comment=comment,
                reason=form.cleaned_data['reason']
            )
            messages.success(request, 'Comment reported successfully!')
            return redirect('exercise_detail', pk=exercise.pk)
        else:
            messages.error(request, 'There was an error reporting the comment. Please try again.')
    else:
        form = ReportCommentForm(
            initial={
                'comment_id': comment.id,
                'comment_text': comment.body,
            }
        )

    return render(request, 'exercises/report_comment_form.html', {'form': form, 'comment': comment})