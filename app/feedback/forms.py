from django import forms
from django.core.exceptions import ValidationError

from feedback.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "category", 'picture')
        labels = {
            'name': 'Название продукта',
            'category': 'Категория',
            'description': 'Описание',
            'picture': 'Фото продукта'
        }

    def clean_name(self):
        product_name = self.cleaned_data.get('product_name')
        if len(product_name) < 3:
            raise ValidationError('Наименование продукта не может состоять из 1 или 2 символов')
        return product_name

    def clean_description(self):
        product_description = self.cleaned_data.get('product_description')
        if len(product_description) < 3 and len(product_description) != 0:
            raise ValidationError('Описание продукта не может состоять из 1 или 2 символов, но может быть пустым')
        return product_description
