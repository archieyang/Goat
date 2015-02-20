# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from Goat.stores.models import Store
from Goat.stores.serializers import StoreSerializer


class StoreSerializeTests(TestCase):
    def test_serialize_store(self):
        store = Store(name=u"外婆家",
                      location=u"北京市海淀区清河中街68号华润五彩城",
                      category=u"餐厅")
        store.save()

        serializer = StoreSerializer(store)
        self.assertEqual(
            {
                'id': store.pk,
                'name': store.name,
                'location': store.location,
                'category': store.category
            },
            serializer.data)


class StoreListTests(TestCase):
    def setUp(self):
        self.url = reverse('stores:list')
        for i in range(3):
            store = Store(name='Store ' + str(i),
                          location='Location ' + str(i),
                          category='Category ' + str(i))
            store.save()

    def test_get_store_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.dumps(StoreSerializer(Store.objects.all(), many=True).data),
                         response.content)