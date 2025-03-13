from django import forms
from .models import Order
from menu.models import Dishes


class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Dishes.objects.all(),)
    
    class Meta:
        model = Order
        fields = ('table_number', 'items')


class OrderStatusForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('В ожидании', 'В ожидании'),
        ('Готово', 'Готово'),
        ('Оплачено', 'Оплачено'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES)
    class Meta:
        model = Order
        fields = ('status', )


class ChangeOrderForm(forms.Form):
    table_number = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': 'readonly'
    }))

    class Meta:
        model = Order
        fields = ('table_number', 'items')