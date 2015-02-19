# -*- coding: utf-8 -*-
from django.test import TestCase
from Goat.stores.models import Store
from Goat.stores.serializers import StoreSerializer


class StoreSerializeTests(TestCase):
    def setUp(self):
        pass

    def test_serialize_store(self):
        store = Store(name=u"外婆家",
                      location=u"北京市海淀区清河中街68号华润五彩城",
                      category=u"餐厅")
        store.save()

        serializer = StoreSerializer(store)
        self.assertEqual(
            {
                'pk': store.pk,
                'name': store.name,
                'location': store.location,
                'category': store.category
            },
            serializer.data)