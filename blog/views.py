from django.shortcuts import render
from django.views.generic import ListView

from models import BlogDetail


class BlogListView(ListView):
    """
    Контроллер для вывода списка статей
    """

    model = BlogDetail
