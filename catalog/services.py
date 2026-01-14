from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """
    Получает данные по продуктам из кеша, если кэш пуст, то получает данные из бд.
    """

    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

def get_category_list(category_name=None):
    """
    Получает список продуктов по категориям.
    """

    products = Product.objects.all().select_related('category')

    if category_name:
        products = products.filter(category__name__icontains=category_name)

    return products.order_by('created_at')