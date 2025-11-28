from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


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
