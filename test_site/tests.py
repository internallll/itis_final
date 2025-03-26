
from rest_framework import status


from rest_framework.test import APITestCase

from test_site.models import User


class UserRegistrationTestCase(APITestCase):

    # регистрации пользователя
    def setUp(self):
        url = '/auth/users/'
        self.data = {
            "full_name": "Иван Иванов",
            "email": "ivan@example.com",
            "password": "strong_password",
        }
        self.client.post(url, self.data, format='json')
        self.user = User.objects.last()

    # Проверка регистрации пользователя
    def test_user_registration(self):
        self.assertEqual(self.user.email, "ivan@example.com")
        self.assertEqual(User.objects.count(), 1)

    # Проверка создания jwt токена
    def test_jwt_get(self):
        url_jwt = '/auth/jwt/create/'
        data_jwt = {
            "email": self.data["email"],
            "password": self.data["password"],
        }
        response_jwt = self.client.post(url_jwt, data_jwt, format='json')
        self.assertEqual(response_jwt.status_code, status.HTTP_200_OK)
        access_token = response_jwt.data['access']
        response_verify = self.client.post('/auth/jwt/verify/', {"token": access_token}, format='json')
        self.assertEqual(response_verify.status_code, status.HTTP_200_OK)

    # Проверка использования refresh токена
    def test_jwt_refresh(self):
        url_jwt = '/auth/jwt/create/'
        data_jwt = {
            "email": self.data["email"],
            "password": self.data["password"],
        }
        response_jwt = self.client.post(url_jwt, data_jwt, format='json')
        self.assertEqual(response_jwt.status_code, status.HTTP_200_OK)
        refresh_jwt = response_jwt.data['refresh']
        response_refresh = self.client.post('/auth/jwt/refresh/', {"refresh": refresh_jwt}, format='json')
        self.assertEqual(response_refresh.status_code, status.HTTP_200_OK)

    # Обновление пользователя
    def test_user_update(self):
        url_update = '/auth/users/me/'
        data_update = {
            "full_name": "Руслан Маратович",
        }
        access_token = \
            self.client.post('/auth/jwt/create/', {"email": self.data["email"], "password": self.data["password"]},
                             format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response_update = self.client.patch(url_update, data_update, format='json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.full_name, "Руслан Маратович")

    # Тест для проверки удаления
    def test_user_delete(self):
        url_delete = '/auth/users/me/'
        access_token = \
        self.client.post('/auth/jwt/create/', {"email": self.data["email"], "password": self.data["password"]}, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response_delete = self.client.delete(url_delete, {"current_password": self.data["password"]}, format='json')
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
