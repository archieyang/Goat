from rest_framework import serializers
from Goat.stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Store
        fields = ['id', 'name', 'location', 'category', 'owner']
