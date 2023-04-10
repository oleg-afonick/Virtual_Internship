import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import PassUser
from users.serializers import PassUserSerializer


class CoordsApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.user_1 = PassUser.objects.create(
            email="Test1@mail.ru",
            lastname="Test1",
            firstname="Test1",
            surname="Test1",
            phone="8-001-001-01-01"
        )
        self.user_2 = PassUser.objects.create(
            email="Test2@mail.ru",
            lastname="Test2",
            firstname="Test2",
            surname="Test2",
            phone="8-002-002-02-02"
        )

    def test_get(self):
        url = reverse('user-list')
        response = self.client.get(url)
        serializer_data = PassUserSerializer([self.user_1, self.user_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())
        self.assertEqual(len(serializer_data), 2)

    def test_get_detail(self):
        url = reverse('user-detail', args=(self.user_1.id,))
        response = self.client.get(url)
        serializer_data = PassUserSerializer(self.user_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_user_reuse(self):
        url = reverse('user-list')
        data = {
            'email': 'Test1@mail.ru',
            'firstname': 'Test1',
            'lastname': 'Test1',
            'surname': 'Test1',
            'phone': '8-001-001-01-01'
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(2, PassUser.objects.all().count())

    def test_create(self):
        url = reverse('user-list')
        data = {
            'email': 'Test3@mail.ru',
            'firstname': 'Test3',
            'lastname': 'Test3',
            'surname': 'Test3',
            'phone': '8-003-003-03-03'
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, PassUser.objects.all().count())


