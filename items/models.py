from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Наименование товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.PositiveIntegerField(validators=[MinValueValidator(50)], verbose_name='Цена товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

