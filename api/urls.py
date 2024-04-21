from django.urls import path, re_path
from . import views
from .views import api_overview

urlpatterns = [
    # API Overview
    path('', api_overview, name='api_overview'),
    re_path('login/', views.login),
    re_path('signup/', views.signup),
    re_path('test_token/', views.test_token),

]
