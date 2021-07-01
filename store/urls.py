from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_type,
    create_drop,
    create_product,
    create_order,
    create_delivery,
    SupplierListView,
    BuyerListView,
    TypeListView,
    DropListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
    update_delivery,
    update_order,
    update_product
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-type/', create_type, name='create-type'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('type-list/', TypeListView.as_view(), name='type-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),

    #edit path
    path('create-delivery/<int:item_id>/', update_delivery, name='update-delivery'),
    path('create-order/<int:item_id>/', update_order, name='update-order'),
    path('create-product/<int:item_id>/', update_product, name='update-product'),
]
