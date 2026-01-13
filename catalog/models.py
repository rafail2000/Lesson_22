from django.db import models

from users.models import User


class Category(models.Model):
    """
    Класс категории
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Класс продукта
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )

    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )

    image = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        null=True,
        blank=True,
        related_name="products",
    )

    price = models.FloatField(verbose_name="Цена", help_text="Введите цену продукта")
    created_at = models.DateField(
        blank=True,
        verbose_name="Дата создания",
        null=True,
        help_text="Введите дату создания",
    )

    updated_at = models.DateField(
        blank=True,
        verbose_name="Дата последнего обновления",
        null=True,
        help_text="Введите дату последнего обновления",
    )

    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        help_text='Укажите имя владельца',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано'
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ('can_unpublish_product', 'Can unpublished product'),
        ]

    def __str__(self):
        return self.name


class Contact(models.Model):
    """
    Модель для хранения контактных данных компании
    """

    country = models.CharField(max_length=100, verbose_name='Страна')
    inn = models.CharField(max_length=20, verbose_name='ИНН')
    address = models.TextField(verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f"Контакты ({self.country})"
