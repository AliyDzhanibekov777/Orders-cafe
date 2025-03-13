from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus

from orders.models import Order
from orders.forms import OrderForm, OrderStatusForm, ChangeOrderForm
from menu.models import Dishes


class OrderViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.item = Dishes.objects.create(name='Борщ', price=210)
        cls.order = Order.objects.create(table_number=1, status='В ожидании')
        cls.order.items.set([cls.item])

    def test_order_list(self):
        url = reverse('orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'orders/home.html')

    def test_create_order_get(self):
        url = reverse('create_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'orders/create_order.html')

    def test_create_order_post_valid(self):
        url = reverse('create_order')
        response = self.client.post(url, {'table_number': 1, 'status': 'Готово'})
        self.assertEqual(Order.objects.count(), 1)
        self.assertIsInstance(response.context['form'], OrderForm)

    def test_create_order_post_invalid(self):
        url = reverse('create_order')
        response = self.client.post(url, {'table_number': 1, 'status': 'Готово'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.context['form'], OrderForm)
        self.assertTrue(response.context['form'].errors)

    def test_delete_order(self):
        url = reverse('delete_order', args=[self.order.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('orders'))
        self.assertEqual(Order.objects.count(), 0)

    def test_search_order(self):
        url = reverse('search_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_change_status_get(self):
        url = reverse('change_status', args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.context['form'], OrderStatusForm)

    def test_change_status_post_valid(self):
        url = reverse('change_status', args=[self.order.id])
        response = self.client.post(url, {'status': 'Оплачено'})
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'Оплачено')
        self.assertRedirects(response, reverse('orders'))

    def test_change_order_get(self):
        url = reverse('change_order', args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.context['form'], OrderForm)

    def test_change_order_post_valid(self):
        url = reverse('change_order', args=[self.order.id])
        response = self.client.post(url, {'table_number': 4})
        self.order.items.set([Dishes.objects.get()])
        self.order.refresh_from_db()
        self.assertEqual(self.order.table_number, 1)

    def test_total_revenue(self):
        response = self.client.get(reverse('total_revenue'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'orders/total_revenue.html')