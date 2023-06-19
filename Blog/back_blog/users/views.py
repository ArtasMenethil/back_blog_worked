from django.contrib.auth import login
from rest_framework import viewsets, generics, permissions, serializers, status
from rest_framework.response import Response
from .models import User
from . import serializers
from rest_framework import views
from .serializers import UserSerializer, LoginSerializer, UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = User.objects.create_user(**serializer.validated_data)
        return Response(self.get_serializer(user).data)

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'retrieve':
            return UserSerializer


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=False)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
