from django.urls import path, re_path
from . import views
from .views import api_overview, UserListView, UserActivityViewSet, UserOnlineView

from django.contrib.auth import views as auth_views    #
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()

#router.register('user-activity', UserActivityViewSet, basename='user-activity')

urlpatterns = [
    # API Overview
    path('', api_overview, name='api_overview'),
    re_path('login/', views.login),
    re_path('signup/', views.signup),
    re_path('test_token/', views.test_token),
    re_path('users/', UserListView.as_view(), name='user-list'),
    re_path('usersOnline/', UserOnlineView.as_view()),
    #re_path('user/<int:pk>/', UserView.as_view(), name='user'),
    #re_path('who/', views.sample_view),

    # forget password :
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


]

#urlpatterns += router.urls
