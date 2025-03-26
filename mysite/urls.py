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
    path('', include('feedback.urls'))



]
