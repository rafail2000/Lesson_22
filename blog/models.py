from django.db import models


class BlogDetail(models.Model):
    """
    Класс модели блога
    """

    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )

    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое статьи"
    )

    preview = models.ImageField(
        upload_to='blog/photo',
        blank=True,
        null=True,
        verbose_name="Превью статьи",
        help_text="Загрузите превью для статьи",
        )

    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    publication_attribute = models.BooleanField(
        default=False
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров",
        default=0
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["created_at"]

    def __str__(self):
        return self.title