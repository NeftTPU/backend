from django.db import models
from django.contrib.auth import get_user_model


class Collection(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    height = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Pattern(models.Model):
    pattern = models.ImageField(upload_to="patterns/")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'


class Pull(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'


class Image(models.Model):
    pull = models.ForeignKey(Pull, on_delete=models.CASCADE)
    pattern = models.ImageField(upload_to="images/")
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
