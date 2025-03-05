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
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView

from test_site import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Login
    path('', include('authentication.urls')),

    # User
    path('api/users/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user-update'),
    path('api/users/<int:pk>/', views.UserDeleteAPIView.as_view(), name='user-delete'),
    path('api/users/', views.UserCreateAPIView.as_view(), name='user-create'),
    path('api/users/list/', views.UserListAPIView.as_view(), name='user-list'),
    # url для получения опросников созданных пользователем
    path('api/users/<int:pk>/feedback/', views.FeedBackUserFilterListAPIView.as_view()),

    # Feedback
    path('api/feedback/<int:pk>/', views.FeedBackUpdateAPIView.as_view(), name='feedback-update'),
    path('api/feedback/', views.FeedBackCreateAPIView.as_view(), name='feedback-create'),
    path('api/feedback/list/', views.FeedBackListAPIView.as_view(), name='feedback-list'),
    path('api/feedback/<int:pk>/', views.FeedBackDeleteAPIView.as_view(), name='feedback-delete'),
    # path('api/feedback/user/<int:pk>', views.FeedBackUserFilterListAPIView.as_view(), name='feedback-filter-user'),
    # представление для просмотра принимающих пользователей
    path('api/feedback/receiver/<int:pk>/', views.FeedbackReceiversListAPIView.as_view(), name='feedback_receivers'),

    # Questions
    path('api/question/feedback/<int:pk>/', views.QuestionListFilterAPIView.as_view(), name='question-list'),
    path('api/question/create/', views.QuestionCreate.as_view(), name='question-create'),
    path('api/question/list/', views.QuestionListAPIView.as_view(), name='question-list'),
    path('api/question/<int:pk>/', views.QuestionUpdateDeleteAPIView.as_view(), name='question-update-delete'),




    # DoneFeedback
    path('api/done_feedback/list/', views.DoneFeedbackListAPIView.as_view(), name='done_feedback-list'),
    path('api/done_feedback/', views.DoneFeedbackCreateAPIView.as_view(), name='done_feedback-create'),
    path('api/done_feedback/<int:pk>/', views.DoneFeedbackUpdateDeleteAPIView.as_view(), name='done_feedback-update-delete'),


    # Answer
    path('api/answer/', views.AnswerView.as_view(), name='answer-create-list'),
    path('api/answer/<int:pk>/', views.AnswerUpdateDeleteView.as_view(), name='answer-update-delete'),




    path('api/choices/', views.ChoicesView.as_view(), name='choices-create'),
    path('api/choices/<int:pk>/', views.ChoicesUpdateDeleteView.as_view(), name='choices-update-delete'),



]
