from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, LikeViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

like_list = LikeViewSet.as_view({'post': 'create'})
like_detail = LikeViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('likes/', like_list, name='likes-list'),
    path('likes/<int:pk>/', like_detail, name='likes-detail'),
    path('', include(router.urls))
]
