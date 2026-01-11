from django.urls import reverse_lazy, reverse
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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    """
    Контроллер для вывода списка статей
    """

    model = BlogDetail
    template_name = "blog/articles_list.html"

    def get_queryset(self):
        return BlogDetail.objects.filter(publication_attribute=True)


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

    def get_success_url(self):
        return reverse("blog:article_detail", args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    """
    Контроллер для удаления статьи
    """

    model = BlogDetail
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("blog:articles_list")
