from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import PostSerializer, LikeSerializer
from api.models import Post, Like

User = get_user_model()


class PostViewSet(ViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(responses={200: PostSerializer(many=True)})
    def list(self, request):
        queryset = Post.objects.filter(is_active=True, user=request.user.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(request_body=PostSerializer)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({
            'data': serializer.data,
            'message': 'success'},
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(responses={200: PostSerializer()})
    def retrieve(self, request, pk=None):
        try:
            post = Post.objects.get(user=request.user.id, pk=pk)
        except Post.DoesNotExist:
            return Response({
                "data": "Post not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(post)
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(request_body=PostSerializer)
    def update(self, request, pk=None):
        try:
            post = Post.objects.get(user=request.user.id, pk=pk)
        except Post.DoesNotExist:
            return Response({
                "data": "Post not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema()
    def destroy(self, request, pk=None):
        try:
            post = Post.objects.get(user=request.user.id, pk=pk)
        except Post.DoesNotExist:
            return Response({
                "data": "Post not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        post.is_active = False
        post.save()
        return Response({
            "message": "success"
            },
            status=status.HTTP_200_OK
        )


class LikeViewSet(ViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=LikeSerializer)
    def create(self, request):
        data = request.data
        try:
            Post.objects.get(user=request.user.id, pk=data['post'])
        except Post.DoesNotExist:
            return Response({
                "data": "Post not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({
            'data': serializer.data,
            'message': 'success'},
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema()
    def destroy(self, request, pk=None):
        try:
            like = Like.objects.get(user=request.user.id, pk=pk)
        except Like.DoesNotExist:
            return Response({
                "data": "Like not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        like.delete()
        return Response({
            "message": "success"
            },
            status=status.HTTP_200_OK
        )
