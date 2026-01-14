from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ContactsFormView, BaseTemplateView, \
    ProductDetailView, ProductsListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsFormView.as_view(), name='contacts'),
    path('product_item/<int:pk>/', cache_page(60 * 15)(ProductDetailView.as_view()), name='product_item'),
    path('products_list/', ProductsListView.as_view(), name='products_list'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
