from django.urls import path, re_path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('books/', views.BookListView.as_view(), name='books'),
        re_path(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
        path('authors/', views.AuthorListView.as_view(), name="authors"),
        re_path(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author_detail'),
        path('my_books/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
        path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
        path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
        path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name="author-update"),
        path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
        path('books/create', views.BookCreate.as_view(), name='book-create'),
        path('books/<int:pk>/update', views.BookUpdate.as_view(), name='book-update'),
        path('books/<int:pk>/delete', views.BookDelete.as_view(), name='book-delete'),
]