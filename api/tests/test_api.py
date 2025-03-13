from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from orders.models import Order

from api.serializers import OrderSerializer


class OrderApiTestCase(APITestCase):
    def test_get(self):
        order_1 = Order.objects.create(table_number=7, status='Готово')
        order_2 = Order.objects.create(table_number=8, status='Готово')
        url = reverse('order-list')
        response = self.client.get(url)
        serializer_data = OrderSerializer([order_1, order_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)