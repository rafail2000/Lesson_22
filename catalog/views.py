from django import forms
# from django.core.paginator import Paginator
from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView, ListView, CreateView

from catalog.models import Product, Contact


class BaseTemplateView(TemplateView):
    """
    Контроллер базовой страницы
    """

    template_name = 'catalog/base.html'


# def base(request):
#     """
#     Контроллер базовой страницы
#     """
#
#     return render(request, 'base.html')


class HomeTemplateView(TemplateView):
    """
    Контроллер главной страницы
    """

    template_name = 'catalog/home.html'

    latest_products = Product.objects.all().order_by('created_at')
    if len(latest_products) > 5:
        latest_products = latest_products[:5]
    print("*****Последние пять продуктов*****")
    for product in latest_products:
        print(product)


# def home(request):
#     """
#     Контроллер страницы home.html
#     """
#
#     latest_products = Product.objects.all().order_by('created_at')
#     if len(latest_products) > 5:
#         latest_products = latest_products[:5]
#     print("*****Последние пять продуктов*****")
#     for product in latest_products:
#         print(product)
#
#     return render(request, 'home.html')


class ContactForm(forms.Form):
    """
    Форма для контактов
    """

    name = forms.CharField(max_length=100, label="Имя")
    phone = forms.CharField(max_length=20, label="Телефон")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")


class ContactsFormView(FormView):
    """
    Контроллер страницы контактов
    """

    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = '/contacts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        return HttpResponse(f'спасибо, {name}! Сообщение получено.')


# def contacts(request):
#     """
#     Контроллер страницы контактов
#     """
#
#     contact_info = Contact.objects.first()
#
#     if request.method =="POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#
#         return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
#     context = {
#         'contact': contact_info
#     }
#     return render(request, 'contacts.html', context)


class ProductDetailView(DetailView):
    """
    Контроллер товара
    """

    model = Product
    template_name = 'catalog/article_detail.html'
    context_object_name = 'product'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_data'] = Product.objects.get(pk=pk)
        return context


# def product_item(request, pk):
#     """
#     Контроллер товара
#     """
#
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, 'article_detail.html', context)


class ProductsListView(ListView):
    """
    Контроллер списка товаров
    """

    model = Product
    template_name = 'catalog/articles_list.html'
    context_object_name = 'products'
    paginate_by = 6
    ordering = ['created_at']

    def get_queryset(self):
        return Product.objects.filter()


# def products_list(request):
#     """
#     Контроллер списка товаров
#     """
#
#     products = Product.objects.all().order_by('created_at')
#     paginator = Paginator(products, 6)
#     page = request.GET.get('page')
#     products_page = paginator.get_page(page)
#     return render(request, 'articles_list.html', {'products': products_page})


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'category', 'price']


class ProductCreateView(CreateView):
    """
    Страница добавления нового товара
    """

    model = Product
    fields = ['name', 'description', 'category', 'price']
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:products_list')


# def add_product(request):
#     """
#     Страница добавления нового товара
#     """
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             messages.success(request, f'Товар "{product.name}" успешно добавлен!')
#             return redirect('/products_list/')  # ← имя маршрута, не шаблона
#     else:
#         form = ProductForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить новый товар'
#     }
#     return render(request, 'add_product.html', context)
