from django.contrib import admin
from django.urls import path, include
from exercises import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', include('django_comments.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),  
    path('', include('exercises.urls')),  
]
