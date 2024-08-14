from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Exercise, Comment  # Import Comment from your models.py
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercises/exercise_list.html'
    context_object_name = 'exercises'

class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'exercises/exercise_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercise = self.get_object()
        context['comments'] = Comment.objects.filter(exercise=exercise).order_by('-created_on')
        context['comment_form'] = CommentForm()  # Ensure this is included
        return context


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

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
def add_comment(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # Set the author to the logged-in user
            comment.exercise = exercise  # Link comment to exercise directly
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )
            return redirect('exercise_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'exercise/add_comment.html', {'form': form})

@login_required
def edit_comment(request, pk, comment_id):
    exercise = get_object_or_404(Exercise, pk=pk)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            # Debugging: Check the redirect action
            print(f"Redirecting to exercise_detail with pk={exercise.pk}")
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'exercises/edit_comment.html', {
        'exercise': exercise,
        'comment': comment,
        'form': form,
    })

@login_required
def delete_comment(request, pk, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST' and comment.author == request.user:
        comment.delete()
    return redirect('exercise_detail', pk=pk)