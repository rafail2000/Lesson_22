import os

from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product


class StyleFormMixin:
    """
    Класс Mixin для стилизации формы
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    """
    Класс формы
    """

    forbidden_text = [
        "казино", "криптовалюта", "крипта",
        "биржа", "дешево", "бесплатно",
        "обман", "полиция", "радар"
    ]

    class Meta:
        model = Product
        fields = '__all__'

    def clean_image(self):
        allowed_extensions = ['.png', '.jpg']

        image = self.cleaned_data.get("image", False)

        if image:
            ext = os.path.splitext(image.name)[1].lower()

            if ext not in allowed_extensions:
                raise ValidationError("Допускаются только расширения JPEG, PNG")

            elif image._size > 5*1024*1024:
                self.add_error('image', 'Загружаемое фото не должно весить больше 5 мегабайт')
            return image


    def clean_price(self):
        price = self.cleaned_data.get("price")
        if float(price) <= 0:
            raise ValidationError('Цена должна быть положительной и больше нуля')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in self.forbidden_text:
            if any([True if i.lower() == word else False for i in name.split()]):
                self.add_error('name', f'name не может содержать слово {word}')
            elif any([True if i.lower() == word else False for i in description.split()]):
                self.add_error('description', f'name не может содержать слово {word}')
