from rest_framework import serializers
from .models import Bucketlist, User, UserActions

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    bucketlists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Bucketlist.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'bucketlists')

# class UserActionsSerializers(serializers.ModelSerializer):

#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Bucketlist
#         fields = ('owner', 'date_created')

class UserActionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserActions
        fields = ('owner_id', 'today_count', 'yesterday_count', 'week_count')