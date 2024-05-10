from django.urls import path, re_path
from . import views
from .views import api_overview, UserListView

from django.contrib.auth import views as auth_views    #

urlpatterns = [
    # API Overview
    path('', api_overview, name='api_overview'),
    re_path('login/', views.login),
    re_path('signup/', views.signup),
    re_path('test_token/', views.test_token),
    re_path('users/', UserListView.as_view(), name='user-list'),

    #path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    #path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


]
