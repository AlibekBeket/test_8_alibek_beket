from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор'
    )
    product = models.ForeignKey(
        to='feedback.Product',
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Товар'
    )
    review_text = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name="Текст отзыва"
    )
    grade = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка"
    )

    def __str__(self):
        return f"{self.product} - {self.grade}"
