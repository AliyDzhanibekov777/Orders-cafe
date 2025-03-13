from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Dishes
from.forms import MenuForm


def menu_list(request):
    menu = Dishes.objects.all()
    context = {
        'title': 'Меню',
        'menu': menu
    }
    return render(request, 'menu/menu.html', context)
    

def create_dish(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('menu'))
    else:
        form = MenuForm()
    context = {
        'title': 'Добавление блюда',
        'form': form
    }
    return render(request, 'menu/create_bish.html', context)


def delete_dish(request, dish_id):
    dish = get_object_or_404(Dishes, id=dish_id)
    dish.delete()
    return HttpResponseRedirect(reverse('menu'))