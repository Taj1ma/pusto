from django.db import models




class Category(models.Model):
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('Какой то слуг',primary_key=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name




class Product(models.Model):
    char = models.CharField('Название', max_length=50)
    text = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE,
                                verbose_name='Автор')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return self.char



