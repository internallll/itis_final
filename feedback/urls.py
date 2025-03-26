from django.urls import path

from feedback import views

urlpatterns = [

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
    path('api/done_feedback/<int:pk>/', views.DoneFeedbackUpdateDeleteAPIView.as_view(),
         name='done_feedback-update-delete'),

    # Answer
    path('api/answer/', views.AnswerView.as_view(), name='answer-create-list'),
    path('api/answer/<int:pk>/', views.AnswerUpdateDeleteView.as_view(), name='answer-update-delete'),

    path('api/choices/', views.ChoicesView.as_view(), name='choices-create'),
    path('api/choices/<int:pk>/', views.ChoicesUpdateDeleteView.as_view(), name='choices-update-delete'),
]
