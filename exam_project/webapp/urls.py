from django.urls import path
from webapp.views import BookListView, AuthorListView, \
    AuthorCreateView, AuthorUpdateView, soft_delete_author, book_download
from django.conf.urls.static import static
from django.conf import settings

app_name = 'webapp'


urlpatterns = [
    path('', BookListView.as_view(), name='main_page'),
    path('author_list', AuthorListView.as_view(), name='author_list'),
    path('author_create', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/update', AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete', soft_delete_author, name='author_delete'),
    path('book/<int:pk>/download', book_download, name='book_download')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
