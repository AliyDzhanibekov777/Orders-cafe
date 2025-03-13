from django.urls import path
from . import views


urlpatterns = [
    path('', views.ordered_list, name='orders'),
    path('create/order/', views.create_order, name='create_order'),
    path('delete/order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('search/order/', views.search_order, name='search_order'),
    path('change/order_status/<int:order_id>/', views.change_status, name='change_status'),
    path('change/orders/<int:order_id>/', views.change_order, name='change_order'),
    path('total/revenue/', views.total_revenue, name='total_revenue'),
]