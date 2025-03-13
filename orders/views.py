from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Order
from .forms import OrderForm, OrderStatusForm, ChangeOrderForm


def ordered_list(request):
    orders = Order.objects.all()
    context = {
        'title': 'Заказы',
        'orders': orders
    }
    return render(request, 'orders/home.html', context)



def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders'))
    else:
        form = OrderForm()

    context = {
        'title': 'Добавление заказа',
        'form': form
    }
    return render(request, 'orders/create_order.html', context)


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return HttpResponseRedirect(reverse('orders'))


def search_order(request):
    query = request.GET.get('search', '')
    if isinstance(query, str):
        if query.isdigit():
            orders = Order.objects.filter(id__icontains=query)
        else:
            orders = Order.objects.filter(status__icontains=query)
    else:
        orders = []
    context = {
        'title': 'Поиск',
        'orders': orders
    }
    return render(request, 'orders/search.html', context)


def change_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form  = OrderStatusForm(data=request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders'))
    else:
        form = OrderStatusForm(instance=order)
    context = {
        'title': 'Изменение статуса заказа',
        'order': order,
        'form': form
    }
    return render(request, 'orders/change_status.html', context)


def change_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form  = OrderForm(data=request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders'))
    else:
        form = OrderForm(instance=order)
    context = {
        'title': 'Изменение заказа',
        'order': order,
        'form': form
    }
    return render(request, 'orders/change_order.html', context)


def total_revenue(request):
    orders = Order.objects.filter(status__icontains='Оплачено')
    result = sum(revenue.total_price for revenue in orders)
    context = {
        'title': 'Выручка за смену',
        'orders': orders,
        'total_price': result
    }
    return render(request, 'orders/total_revenue.html', context)