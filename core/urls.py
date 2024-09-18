from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('files/', views.list_uploaded_files, name='list_uploaded_files'),
]


urlpatterns += static (settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)