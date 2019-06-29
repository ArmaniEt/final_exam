from django.urls import path
from webapp.views import BookListView, AuthorListView, \
    AuthorCreateView, AuthorUpdateView, soft_delete_author, \
    book_download, BookCreateView, BookUpdateView, BookDeleteView, \
    AuthorDetailView, UserListView, UserDetailView, add_book_to_shelf, delete_book_from_shelf
from django.conf.urls.static import static
from django.conf import settings

app_name = 'webapp'


urlpatterns = [

    path('', BookListView.as_view(), name='main_page'),
    # author url's
    path('author_list', AuthorListView.as_view(), name='author_list'),
    path('author_create', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/update', AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete', soft_delete_author, name='author_delete'),
    path('author/<int:pk>/view', AuthorDetailView.as_view(), name='author_detail'),
    # book url's
    path('book/<int:pk>/download', book_download, name='book_download'),
    path('book_create', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    # user url's
    path('user_list', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('add_book_to_shelf', add_book_to_shelf, name='add_book'),
    path('delete_book_from_shelf', delete_book_from_shelf, name='delete_book')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
