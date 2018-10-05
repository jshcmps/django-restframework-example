from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()