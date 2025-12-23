from django import forms
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class BaseTemplateView(TemplateView):
    """
    Контроллер базовой страницы
    """

    template_name = 'catalog/base.html'


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


class ProductDetailView(DetailView):
    """
    Контроллер товара
    """

    model = Product
    template_name = 'catalog/product_item.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['additional_data'] = Product.objects.get(pk=pk)
        return context


class ProductsListView(ListView):
    """
    Контроллер списка товаров
    """

    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'
    paginate_by = 6
    ordering = ['created_at']

    def get_queryset(self):
        return Product.objects.filter()


class ProductCreateView(CreateView):
    """
    Страница добавления нового товара
    """

    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    """
    Страница редактирования имеющегося товара
    """

    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
    """
    Страница удаления имеющегося товара
    """

    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')

