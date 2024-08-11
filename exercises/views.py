from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/exercise_list.html', {'exercises': exercises})

def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'exercises/exercise_detail.html', {'exercise': exercise})

@login_required
def add_comment(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.exercise = exercise
            comment.save()
            return redirect('exercise_detail', pk=pk)
    return redirect('exercise_detail', pk=pk)

@login_required
def edit_comment(request, pk, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('exercise_detail', pk=pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'exercises/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, pk, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('exercise_detail', pk=pk)
    return render(request, 'exercises/delete_comment.html', {'comment': comment})
