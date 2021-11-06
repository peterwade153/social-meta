from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import (
    MetaTokenObtainPairSerializer,
    RegisterSerializer,
    UserSerializer
)
from authentication.tasks import validate_user_email, update_user_geo_data

User = get_user_model()


class EmailTokenObtainPairViewSet(TokenObtainPairView):
    serializer_class = MetaTokenObtainPairSerializer


class UserRegistrationViewSet(ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]

    @swagger_auto_schema(request_body=RegisterSerializer)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        validate_user_email.delay(email=data['email'])
        update_user_geo_data(email=data['email'])
        return Response({
            "data": data,
            "message": "success"
            },
            status=status.HTTP_201_CREATED
        )

class UsersListViewSet(ViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(responses = {200: UserSerializer(many=True)})
    def list(self, request):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )

