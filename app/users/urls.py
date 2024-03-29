from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),

    path('logout/', LogoutView.as_view(), name="logout"),
    
    path('register', UserReg.as_view(), name="register"),

    path('profile/', UserProfile, name="profile"),

    path('profile-edit/', EditUser, name="user_edit"),

    path('admin-page/', AdminPage, name="admin_page"),

    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
