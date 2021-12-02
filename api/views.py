from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
from django.http.response import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import PostSerializer, LikeSerializer
from api.models import Post, Like

User = get_user_model()


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True, user=self.request.user)

    def get_object(self):
        try:
            return Post.objects.get(user=self.request.user.id, pk=self.kwargs['pk'])
        except Post.DoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
