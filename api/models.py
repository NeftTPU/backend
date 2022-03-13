from django.db import models
from django.contrib.auth import get_user_model


class Image(models.Model):
    file = models.ImageField(upload_to="images/")
    date_created = models.DateField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


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


class Layer(models.Model):
    title = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Слой'
        verbose_name_plural = 'Слои'


class Pool(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_generated = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    collections = models.ManyToManyField(Collection)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'