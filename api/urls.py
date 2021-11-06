from django.urls import path

from api.views import PostViewSet, LikeViewSet

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

like_list = LikeViewSet.as_view({'post': 'create'})
like_detail = LikeViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('posts/', post_list, name='posts'),
    path('posts/<int:pk>/', post_detail, name='posts-detail'),
    path('likes/', like_list, name='likes-list'),
    path('likes/<int:pk>/', like_detail, name='likes-detail'),
]
