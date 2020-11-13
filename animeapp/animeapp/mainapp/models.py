from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Manga(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    photo = models.ImageField('Картинка', upload_to='static/img', height_field=None, width_field=None, max_length=100,
                              null=True)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    avtor = models.CharField(max_length=128)
    painter = models.CharField(max_length=128)
    data = models.DateField()
    page = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'

class Anime(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    photo = models.ImageField('Картинка', upload_to='static/img', height_field=None, width_field=None, max_length=100,
null=True)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    producer = models.CharField(max_length=128)
    data = models.DateField()
    episodes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'