from django.contrib import admin
from .models import Exercise,Comment

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'image')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

admin.site.register(Comment)