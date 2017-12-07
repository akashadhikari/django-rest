from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import BucketlistSerializer, UserSerializer, UserActionsSerializers
from .models import Bucketlist, User

from rest_framework import permissions

def index(request):
    return HttpResponse("You're looking at question")

class CreateView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserActionsView(generics.ListAPIView):
    """View to list the user queryset."""
    # queryset = User.objects.filter(id=1)
    queryset = Bucketlist.objects.raw('SELECT * FROM api_bucketlist')
    serializer_class = UserActionsSerializers

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer