from rest_framework import serializers

from api.models import Post, Like


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ['id', 'user', 'is_active']
        fields = ['text'] + read_only_fields


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        read_only_fields = ['id', 'user']
        fields = ['post'] + read_only_fields
