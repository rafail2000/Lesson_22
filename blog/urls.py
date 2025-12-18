from django.urls import path
from catalog.apps import CatalogConfig
from blog.views import BlogListView, BaseTemplateView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base'),
    path('article_detail/<int:pk>/', BlogDetailView.as_view(), name='article_detail'),
    path('articles_list/', BlogListView.as_view(), name='articles_list'),
    path('create/', BlogCreateView.as_view(), name='article_create'),
    path('/<int:pk>/update/', BlogUpdateView.as_view(), name='article_update'),
    path('/<int:pk>/delete/', BlogDeleteView.as_view(), name='article_delete'),
]
