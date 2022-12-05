from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..serializer.register import RegisterSerializer


class RegisterSerializer(generics.CreateAPIView):
    permission_classes = (AllowAny)
    serializer_class = RegisterSerializer
