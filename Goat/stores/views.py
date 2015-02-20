from rest_framework import generics

from Goat.stores.models import Store
from Goat.stores.serializers import StoreSerializer


class StoreList(generics.ListCreateAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
