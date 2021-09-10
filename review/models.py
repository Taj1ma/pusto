
from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
User = get_user_model()
# Create your models here.
RATING_CHOICES = [
    (1, 'LOW'),

    (2, 'NORMAL'),

    (3, 'GOOD'),

    (4, 'HIGH'),

    (5, 'SUPER'),
]



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField('Текст')
    rating = models.IntegerField('RATING_CHOICES')

    class Meta:
        verbose_name_plural = 'Рассмотрение'