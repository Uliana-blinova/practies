from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Получаем количество объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    # Количество книг, содержащих слово
    search_word = "war"  # вы можете изменить это слово
    num_books_with_word = Book.objects.filter(title__icontains=search_word).count()

    # Счётчик посещений
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Передаём данные в шаблон
    return render(
        request,
        'catalog/index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_books_with_word': num_books_with_word,
            'search_word': search_word,
            'num_visits': num_visits,  # num_visits appended
        },
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author