from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus

from orders.models import Order
from menu.models import Dishes


class TestRoutes(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.item = Dishes.objects.create(name='Шаурма', price=220)
        cls.order = Order.objects.create(table_number=1, status='Оплачено')
        cls.order.items.set([cls.item])

    def test_pages_availability(self):
        urls = (
            ('orders', None),
            ('create_order', None),
            ('search_order', None),
            ('change_status', (self.order.id,)),
            ('change_order', (self.order.id,)),
            ('total_revenue', None)
        )
        for name, args in urls:
            with self.subTest(name=name):
                url = reverse(name, args=args)
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_delete_order_page(self):
        order_url = reverse('orders')
        url = reverse('delete_order', args=(self.order.id,))
        redirect_url = f'{order_url}'
        response = self.client.get(url)
        self.assertRedirects(response, redirect_url)


    # def test_home_page(self):
    #     url = reverse('orders')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)