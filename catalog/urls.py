from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, base, products_list, product_item

app_name = CatalogConfig.name

urlpatterns = [
    path('', base, name='base'),
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_item/<int:pk>/', product_item, name='product_item'),
    path('products_list/', products_list, name='products_list'),
]
