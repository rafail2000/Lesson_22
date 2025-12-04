from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from catalog.models import Product, Contact


def base(request):
    """
    Контроллер базовой страницы
    """

    return render(request, 'base.html')


def home(request):
    """
    Контроллер страницы home.html
    """

    latest_products = Product.objects.all().order_by('created_at')
    if len(latest_products) > 5:
        latest_products = latest_products[:5]
    print("*****Последние пять продуктов*****")
    for product in latest_products:
        print(product)

    return render(request, 'home.html')


def contacts(request):
    """
    Контроллер страницы контактов
    """

    contact_info = Contact.objects.first()

    if request.method =="POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    context = {
        'contact': contact_info
    }
    return render(request, 'contacts.html', context)

def product_item(request, pk):
    """
    Контроллер товара
    """

    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'product_item.html', context)


def products_list(request):
    """
    Контроллер списка товаров
    """

    products = Product.objects.all().order_by('created_at')
    context = {"products": products}
    return render(request, 'products_list.html', context)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']


def add_product(request):
    """
    Страница добавления нового товара
    """

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Товар "{product.name}" успешно добавлен!')
            return redirect('/products_list/')  # ← имя маршрута, не шаблона
    else:
        form = ProductForm()

    context = {
        'form': form,
        'title': 'Добавить новый товар'
    }
    return render(request, 'add_product.html', context)
