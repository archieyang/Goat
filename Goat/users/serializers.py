from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    stores = serializers.HyperlinkedIdentityField(many=True,
                                                  view_name='store-detail',
                                                  read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'stores']