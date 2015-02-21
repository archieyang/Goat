# -*- coding: utf-8 -*-
import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from Goat.stores.models import Store
from Goat.stores.serializers import StoreSerializer


class StoreSerializeTests(TestCase):
    def test_serialize_store(self):
        user = User.objects.create_user(username='archieyang', password='abcdef', email='yangyxcn@gmail.com')
        user.save()
        store = Store.objects.create(name=u"外婆家",
                                     location=u"北京市海淀区清河中街68号华润五彩城",
                                     category=u"餐厅",
                                     owner=user)
        store.save()

        serializer = StoreSerializer(store)
        self.assertEqual(
            {
                'id': store.pk,
                'name': store.name,
                'location': store.location,
                'category': store.category,
                'owner': user.username
            },
            serializer.data)


class StoreListTests(TestCase):
    def setUp(self):
        self.url = reverse('store-list')
        user = User.objects.create_user(username='archieyang', password='abcdef', email='yangyxcn@gmail.com')
        user.save()
        for i in range(3):
            store = Store.objects.create(name='Store ' + str(i),
                                         location='Location ' + str(i),
                                         category='Category ' + str(i),
                                         owner=user)
            store.save()

    def test_get_store_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JSONRenderer().render(StoreSerializer(Store.objects.all(), many=True).data),
                         response.content)


class StoreCreateTest(TestCase):
    def setUp(self):
        self.url = reverse('store-list')
        user = User.objects.create_user(username='archieyang', password='abcdef', email='yangyxcn@gmail.com')
        user.save()

    def test_create_store_success(self):
        store_data = {
            'name': 'Store',
            'location': 'Location',
            'category': 'Category'
        }

        self.client.login(username='archieyang', password='abcdef')
        response = self.client.post(
            self.url,
            json.dumps(store_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.content, JSONRenderer().render(StoreSerializer(Store.objects.last()).data))

    def test_create_store_no_logged_in(self):
        store_data = {
            'name': 'Store',
            'location': 'Location',
            'category': 'Category'
        }

        response = self.client.post(
            self.url,
            json.dumps(store_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RetrieveUpdateDestroyStoreTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='archieyang', password='abcdef', email='yangyxcn@gmail.com')
        self.user.save()

        self.store = Store.objects.create(name=u"外婆家",
                                     location=u"北京市海淀区清河中街68号华润五彩城",
                                     category=u"餐厅",
                                     owner=self.user)
        self.store.save()

    def test_retrieve_store(self):
        response = self.client.get(reverse('store-detail', args=(1,)))
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)
        self.assertEqual(response.content,
                         JSONRenderer().render(StoreSerializer(Store.objects.last()).data))

    def test_update_store_not_logged_in(self):
        store_data = {
            'name': 'Store',
            'location': 'Location',
            'category': 'Category'
        }
        response = self.client.put(reverse('store-detail', args=(1,)),
                                   json.dumps(store_data),
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.store.name, Store.objects.last().name)

    def test_update_success(self):
        store_data = {
            'name': 'Store',
            'location': 'Location',
            'category': 'Category'
        }
        self.client.login(username='archieyang', password='abcdef')
        response = self.client.put(reverse('store-detail', args=(1,)),
                                   json.dumps(store_data),
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, JSONRenderer().render(StoreSerializer(Store.objects.last()).data))
        self.assertNotEqual(self.store.name, Store.objects.last().name)

    def test_delete_store_not_logged_in(self):
        response = self.client.delete(reverse('store-detail', args=(1,)),)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Store.objects.all().count(), 1)

    def test_delete_success(self):
        self.client.login(username='archieyang', password='abcdef')
        response = self.client.delete(reverse('store-detail', args=(1,)),)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Store.objects.all().count(), 0)

