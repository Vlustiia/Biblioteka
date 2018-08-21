from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_special_books = Book.objects.filter(title__contains='колоб').count()

    # метод all() применен по-умолчанию
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1



    #отрисовка HTML шаблона
    return render(
        request,
        'index.html',
        context={'num_books':num_books,
                 'num_instances':num_instances,
                 'num_instances_available':num_instances_available,
                 'num_author':num_authors,
                 'num_special_books':num_special_books,
                 'num_genres':num_genres,
                 'num_visits':num_visits,
                 }
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4



class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).\
            filter(status__exact='o').order_by('due_back')


class LoanedBooksAllUsersListView(PermissionRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to all users
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_all_users.html'
    paginate_by = 10
    permission_required = ('catalog.can_mark_returned')

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')