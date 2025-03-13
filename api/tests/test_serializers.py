from api.serializers import OrderSerializer

from django.test import TestCase

from orders.models import Order


class OrderSerializerTestCase(TestCase):
    def test_positiv(self):
        order_1 = Order.objects.create(table_number=7, status='Готово')
        order_2 = Order.objects.create(table_number=8, status='Готово')
        data = OrderSerializer([order_1, order_2], many=True).data
        expected_data = [
            {
                'id': order_1.id,
                'table_number': 7,
                'items': [],
                'status': 'Готово'
            },
            {
                'id': order_2.id,
                'table_number': 8,
                'items': [],
                'status': 'Готово'
            },
        ]
        self.assertEqual(expected_data, data)