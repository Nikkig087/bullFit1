from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Exercise, Comment
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

class ExerciseListView(generic.ListView):
    model = Exercise
    template_name = 'exercises/exercise_list.html'
    context_object_name = 'exercises'
    paginate_by = 6  # Optional: Paginate if you have many exercises

def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    comments = exercise.comments.all().order_by("-created_on")
    comment_count = comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.exercise = exercise
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            return redirect('exercise_detail', pk=pk)  # Redirect to the same view to display messages
    else:
        comment_form = CommentForm()

    return render(
        request,
        "exercises/exercise_detail.html",
        {
            "exercise": exercise,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def edit_comment(request, pk, comment_id):
    exercise = get_object_or_404(Exercise, pk=pk)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'exercises/edit_comment.html', {
        'exercise': exercise,
        'comment': comment,
        'form': form,
    })

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
            messages.success(request, 'Your comment has been added and is awaiting approval.')
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = CommentForm()

    return render(request, 'exercises/add_comment.html', {'form': form, 'exercise': exercise})

@login_required
def delete_comment(request, pk, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST' and comment.user == request.user:  # Ensuring the user is the author
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment successfully deleted'
        )
    return redirect('exercise_detail', pk=pk)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or any other page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})