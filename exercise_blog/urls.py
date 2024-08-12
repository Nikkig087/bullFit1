from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from exercises import views  # Import views from the exercises app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', include('django_comments.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('signup/', views.signup, name='signup'),  # Signup URL
    path('edit_comment/', views.edit_comment, name ='edit_comment'),
    path('', include('exercises.urls')),
    path('registration/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
   # path('comments/', include('django_comments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
