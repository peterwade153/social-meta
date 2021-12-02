from rest_framework import status

from . import BaseAPITestCase, PostFactory


class PostTestCase(BaseAPITestCase):

    def test_create_posts(self):
        data = {
            'text': 'qwerty aghsfff djfjddkjksd'
        }
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post('/api/posts/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get('/api/posts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_post_by_id(self):
        post = PostFactory(
            text='myu muyu',
            user=self.user
        )
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(f'/api/posts/{post.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_posts(self):
        data = {
            'text': 'qwerty aghsfff djfjddkjksd'
        }
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.put(f'/api/posts/{self.post.id}/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_posts(self):
        post = PostFactory(
            text='dsddijidjjdwjfieefw',
            user=self.user
        )
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.delete(f'/api/posts/{post.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
