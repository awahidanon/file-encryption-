from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views

urlpatterns = [
    path("", views.upload_file, name="upload_file"),
    path("download/<int:file_id>/", views.download_file, name="download_file"),
    path("files/", views.list_uploaded_files, name="list_uploaded_files"),
    path(
        "view_encrypted/<int:file_id>/",
        views.view_encrypted_file,
        name="view_encrypted_file",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html",
            success_url=reverse_lazy("list_uploaded_files"),
        ),
        name="login",
    ),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("profile/", views.profile, name="profile"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('share/<int:file_id>/', share_file, name='share_file'),
    path('access/<uuid:token>/', access_shared_file, name='access_shared_file'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
