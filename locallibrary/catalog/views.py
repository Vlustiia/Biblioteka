from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_special_books = Book.objects.filter(title__contains='колоб').count()

    # метод all() применен по-умолчанию
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    #отрисовка HTML шаблона
    return render(
        request,
        'index.html',
        context={'num_books':num_books,
                 'num_instances':num_instances,
                 'num_instances_available':num_instances_available,
                 'num_author':num_authors,
                 'num_special_books':num_special_books,
                 'num_genres':num_genres
                 },
    )

class BookListView(generic.ListView):
    model = Book