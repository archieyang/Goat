from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Goat.stores.models import Store
from Goat.stores.serializers import StoreSerializer


def get_index(request):
    return HttpResponse("hello world")


def store_list(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return None
