from django.urls import path, re_path, include
from . import views
from .views import AllBorrowedBooksListView


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('authors', views.AuthorListView.as_view(), name='authors'),
    path('author/<pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('borrowed/', AllBorrowedBooksListView.as_view(), name='all-borrowed'),
]
urlpatterns += [
    path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
urlpatterns += [
    path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]