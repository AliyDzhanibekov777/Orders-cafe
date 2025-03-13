from django.urls import path

from . import views


urlpatterns = [
    path('v1/order/', views.OrderAPIList.as_view(), name='order-list'),
    path('v1/order/<int:pk>/', views.OrderAPIUpdate.as_view(), name='order-detail'),
    path('v1/order/delete/<int:pk>/', views.OrderAPIDestroy.as_view(), name='order-delete'),
]