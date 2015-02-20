from rest_framework import generics
from rest_framework import mixins

from Goat.stores.models import Store
from Goat.stores.serializers import StoreSerializer


class StoreList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
