from rest_framework import status

from . import BaseAPITestCase, PostFactory, LikeFactory


class LikePostTestCase(BaseAPITestCase):

    def test_like_post(self):
        post = PostFactory(
            text='myu muyu',
            user=self.user
        )
        data = {'post': post.id}
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post('/api/likes/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unlike_post(self):
        post = PostFactory(
            text='myu muyu',
            user=self.user
        )
        like = LikeFactory(
            post=post,
            user=self.user
        )
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.delete(f'/api/likes/{like.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unlike_with_no_exisiting_like(self):
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.delete('/api/likes/1234/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_like_non_existing_post(self):
        data = {'post': 123}
        res = self.login_user()
        token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post('/api/likes/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
