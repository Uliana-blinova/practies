from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Количество жанров
    num_genres = Genre.objects.count()

    # Количество книг
    search_word = "war"  # вы можете изменить это слово
    num_books_with_word = Book.objects.filter(title__icontains=search_word).count()


    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'catalog/index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            # --- НОВОЕ ---
            'num_genres': num_genres,
            'num_books_with_word': num_books_with_word,
            'search_word': search_word,
        },
    )
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
class BookDetailView(generic.DetailView):
    model = Book