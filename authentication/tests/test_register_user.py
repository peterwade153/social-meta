import factory
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class RegisterUserTestCase(APITestCase):

    def test_register_user(self):
        data = {
            "email": "wnewtest@gmail.com",
            "password": "123456POIT",
            "confirm_password": "123456POIT",
        }
        response = self.client.post('/auth/register/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_with_existing_email(self):
        UserFactory(
            email='qwerty@gmail.com',
            password='1234509876'
        )
        data = {
            "email": "qwerty@gmail.com",
            "password": "123456POIT",
            "confirm_password": "123456POIT",
        }
        response = self.client.post('/auth/register/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

