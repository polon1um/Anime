from django.contrib import admin

from mainapp.models import Category
from mainapp.models import Manga
from mainapp.models import Anime


admin.site.register(Category)
admin.site.register(Manga)
admin.site.register(Anime)