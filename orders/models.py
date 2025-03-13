from django.db import models
from menu.models import Dishes
      

class Order(models.Model):
    table_number = models.PositiveSmallIntegerField()
    items = models.ManyToManyField(Dishes)
    status = models.CharField(max_length=30, default='В ожидании')

    @property
    def total_price(self):
        return sum(item.price for item in self.items.all())
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Номер заказа {self.id}'