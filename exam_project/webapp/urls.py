from django.urls import path
from webapp.views import BookListView, AuthorListView, \
    AuthorCreateView, AuthorUpdateView, soft_delete_author, book_download, BookCreateView
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
    # book url's
    path('book/<int:pk>/download', book_download, name='book_download'),
    path('book_create', BookCreateView.as_view(), name='book_create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
