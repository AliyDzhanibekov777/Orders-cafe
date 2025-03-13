from django.contrib import admin
from orders.models import Dishes, Order


admin.site.register(Dishes)
admin.site.register(Order)