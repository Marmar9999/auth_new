from django.urls import path, re_path
from . import views
from .views import *
from django.contrib.auth import views as auth_views    #


urlpatterns = [
    # API Overview
    path('', api_overview, name='api_overview'),
    re_path('login/', views.login),
    re_path('signup/', views.signup),
    re_path('logout/', views.logout_user),
    re_path('test_token/', views.test_token),
    re_path('add_user/', views.addUser),            #to add users manually
    path('suspend_users/',views.suspend_users),      #to change user status
    re_path('users/', UserListView.as_view(), name='user-list'),
    path('change_password/', change_password, name='change_password'),
    # forget password :
    path('external-link/', external_link_view, name='external-link-url'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('accounts/reset/done/', MyPasswordResetCompleteView.as_view(), name="password_reset_complete"),


]

#urlpatterns += router.urls
