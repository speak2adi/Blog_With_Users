from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView,
                                       PasswordResetDoneView, PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetCompleteView, )

urlpatterns = [
    path('register/', views.register, name="registration"),
    path('profile/', views.profile, name="profile"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password_reset/',
         PasswordResetView.as_view(template_name='users/password_reset.html'),
         name="password_reset"),

    path('password_reset/done',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name="password_reset_done"),

    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name="password_reset_confirm"),

    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name="password_reset_complete"),

    path('password_change/',
         PasswordChangeView.as_view(
             template_name='users/password_change.html',
             success_url='/'
         ),
         name="change-password"),

    path('password_change_done/',
         PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name="change-password-done"),
]

# setting up urlpatterns for static media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
