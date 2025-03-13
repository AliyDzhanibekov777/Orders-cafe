from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu_list, name='menu'),
    path('create/dish', views.create_dish, name='create_dish'),
    path('delete/dish/<int:dish_id>', views.delete_dish, name='delete_dish'),
]