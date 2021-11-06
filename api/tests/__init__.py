import factory
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from api. models import Post, Like

User = get_user_model()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post


class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Like


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='qwerty@gmail.com',
            password='1234509876',
        )
        self.user.is_active = True
        self.user.save()

        self.post = PostFactory(
            text='dsddijijfieefw',
            user=self.user
        )

    def login_user(self):
        data = {
            'email': 'qwerty@gmail.com',
            'password': '1234509876'
        }
        return self.client.post('/auth/token/', data)
