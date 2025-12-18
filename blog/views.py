from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogDetail


class BaseTemplateView(TemplateView):
    """
    Контроллер для вывода базового шаблона
    """

    model = BlogDetail
    template_name = "blog/base.html"
    context_object_name = "base"


class BlogDetailView(DetailView):
    """
    Контроллер для вывода статьи
    """

    model = BlogDetail
    template_name = "blog/article_detail.html"
    context_object_name = "base"


class BlogListView(ListView):
    """
    Контроллер для вывода списка статей
    """

    model = BlogDetail
    template_name = "blog/articles_list.html"


class BlogCreateView(CreateView):
    """
    Контроллер для создания статей
    """

    model = BlogDetail
    template_name = "blog/article_form.html"
    fields = ("title", "content", "preview", "publication_attribute")
    success_url = reverse_lazy("blog:articles_list")


class BlogUpdateView(UpdateView):
    """
    Контроллер для создания статей
    """

    model = BlogDetail
    template_name = "blog/article_form.html"
    fields = ("title", "content", "preview", "publication_attribute")
    success_url = reverse_lazy("blog:articles_list")


class BlogDeleteView(DeleteView):
    """
    Контроллер для удаления статьи
    """

    model = BlogDetail
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("blog:articles_list")