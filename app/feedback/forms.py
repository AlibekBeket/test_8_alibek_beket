from django import forms
from django.core.exceptions import ValidationError

from feedback.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "category", "description", "picture")
        labels = {
            'name': 'Название продукта',
            'category': 'Категория',
            'description': 'Описание',
            'picture': 'Фото продукта',
        }

    def clean_name(self):
        product_name = self.cleaned_data.get('name')
        if len(product_name) < 3:
            raise ValidationError('Наименование продукта не может состоять из 1 или 2 символов')
        return product_name

    def clean_description(self):
        product_description = self.cleaned_data.get('description')
        if len(product_description) < 3 and len(product_description) != 0:
            raise ValidationError('Описание продукта не может состоять из 1 или 2 символов, но может быть пустым')
        return product_description

    def clean_picture(self):
        product_picture = self.cleaned_data.get('picture')
        if not product_picture:
            return ''
        return product_picture


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("review_text", "grade")
        labels = {
            'review_text': 'Текст отзыва',
            'grade': 'Оценка',
        }

    def clean_review_text(self):
        review_text = self.cleaned_data.get('review_text')
        if len(review_text) < 3:
            raise ValidationError('Текст отзыва не может состоять из 1 или 2 символов')
        return review_text
