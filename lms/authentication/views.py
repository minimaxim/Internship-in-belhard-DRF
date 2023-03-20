from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import RegisterSerializer, ChangePasswordSerializer
from rest_framework import generics
from .permissions import IsAdmin, IsAdminOrManager, IsAdminOrManagerOrMentor


class MyObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAdminOrManager,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAdmin,)
    serializer_class = ChangePasswordSerializer