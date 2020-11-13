"""animeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import mainapp.views as mainapp

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', mainapp.index),
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('catalog/', mainapp.catalog),
    path('catalog/manga/<int:pk>/', mainapp.manga, name='manga'),
    path('catalog/manga/manga_page<int:pk>/', mainapp.manga_page, name='manga_page'),
    path('catalog/anime/<int:pk>/', mainapp.anime, name='anime'),
    path('catalog/anime/anime_page<int:pk>/', mainapp.anime_page, name='anime_page'),
]
