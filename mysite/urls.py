"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from test_site import views
from test_site.views import QuestionListAPIView



urlpatterns = [
    path('admin/', admin.site.urls),

    #User
    path('api/users/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user-update'),
    path('api/users/delete/<int:pk>/', views.UserDeleteAPIView.as_view(), name='user-delete'),
    path('api/users/create/', views.UserCreateAPIView.as_view(), name='user-create'),
    path('api/users/list/', views.UserListAPIView.as_view(), name='user-list'),

    #Feedback
    path('api/feedback/<int:pk>', views.FeedBackUpdateAPIView.as_view(), name='feedback-update'),
    path('api/feedback/create/', views.FeedBackCreateAPIView.as_view(), name='feedback-create'),
    path('api/feedback/list/', views.FeedBackListAPIView.as_view(), name='feedback-list'),
    path('api/feedback/delete/<int:pk>', views.FeedBackDeleteAPIView.as_view(), name='feedback-delete'),
    path('api/feedback/user/<int:pk>', views.FeedBackUserFilterListAPIView.as_view(), name='feedback-filter-user'),

    #Questions
    path('api/question/feedback/<int:pk>', views.QuestionListAPIView.as_view(), name='question-list'),


]
