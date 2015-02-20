from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Goat.stores.models import Store
from Goat.stores.serializers import StoreSerializer


class StoreList(APIView):
    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
