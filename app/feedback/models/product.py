from django.db import models
from django.db.models import TextChoices


class ProductCategoryChoice(TextChoices):
    OTHER = 'other', 'Разное'
    FOOD = 'food', 'Еда'
    ELECTRONICS = 'electronics', 'Электроника'
    DISHES = 'dishes', 'Посуда'


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Имя"
    )
    category = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Категория',
        choices=ProductCategoryChoice.choices,
        default=ProductCategoryChoice.OTHER
    )
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    picture = models.URLField(
        max_length=10000,
        null=True,
        blank=True,
        verbose_name="Картинка"
    )

    def __str__(self):
        return f"{self.name} - {self.category}"
