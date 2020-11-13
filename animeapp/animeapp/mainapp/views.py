from django.shortcuts import render

from mainapp.models import Category, Manga, Anime


def catalog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }

    return render(request, 'mainapp/catalog.html', context)


def index(request):
    return render(request, 'mainapp/index.html')


def manga(request, pk):
    Manges = Manga.objects.filter(category_id=pk)
    context = {
        'Manges': Manges,
        'page_title': 'Манга'
    }
    return render(request, 'mainapp/manga.html', context)

def manga_page(request, pk):
    manga = Manga.objects.get(pk=pk)
    context = {
        'manga': manga,
        'page_title': 'Манга'
    }
    return render(request, 'mainapp/manga_page.html', context)


def anime(request, pk):
    Animes = Anime.objects.filter(category_id=pk)
    context = {
        'Animes': Animes,
        'page_title': 'Аниме'
    }
    return render(request, 'mainapp/anime.html', context)

def anime_page(request, pk):
    anime = Anime.objects.get(pk=pk)
    context = {
        'anime': anime,
        'page_title': 'Аниме'
    }
    return render(request, 'mainapp/anime_page.html', context)