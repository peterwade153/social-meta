from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


User = get_user_model()


class ListUsersTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='qwerty@gmail.com',
            password='1234509876',
        )
        self.user.is_active = True
        self.user.save()

    def test_list_users(self):
        data = {
            'email': 'qwerty@gmail.com',
            'password': '1234509876'
        }
        res = self.client.post('/auth/token/', data)
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get('/auth/users/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
