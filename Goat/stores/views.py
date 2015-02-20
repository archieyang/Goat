from rest_framework import generics, permissions

from Goat.stores.models import Store
from Goat.stores.permissions import isOwnerOrReadOnly
from Goat.stores.serializers import StoreSerializer


class StoreList(generics.ListCreateAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
