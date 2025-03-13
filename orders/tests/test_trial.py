from django.test import TestCase

from unittest import skip

from orders.models import Order
from menu.models import Dishes

@skip #Этот декоратор делает так, чтобы при запуске тестов, командная строка не видела обернутый класс.
# Тем самым эти тесты у нас не будут работать.
class TestOrders(TestCase):
    STATUS = 'Готово'
    
    @classmethod
    def setUpTestData(cls):
        cls.item = Dishes.objects.create(
            name='Уха', 
            price=220
        )

        cls.order = Order.objects.create(
            table_number=5,
            status=cls.STATUS
        )
        cls.order.items.set([cls.item])

    def test_successful_creations(self):
        orders_count = Order.objects.count()
        self.assertEqual(orders_count, 1)

    def test_status(self):
        self.assertEqual(self.order.status, self.STATUS)