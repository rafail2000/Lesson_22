from django.contrib import admin
from catalog.models import Product, Category, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('country', 'inn', 'address', 'phone', 'email', 'updated_at')
    list_filter = ('country',)
    search_fields = ('country', 'inn', 'address')

