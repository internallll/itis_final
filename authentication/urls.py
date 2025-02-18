from django.urls import path

from authentication.views import CustomAuthToken, RegistrationAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    ]