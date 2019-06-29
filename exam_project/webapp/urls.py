from django.urls import path
from webapp.views import MainPage, AuthorListView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'webapp'


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('author_list', AuthorListView.as_view(), name='author_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
