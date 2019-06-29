from django.urls import path
from webapp.views import MainPage
from django.conf.urls.static import static
from django.conf import settings

app_name = 'webapp'


urlpatterns = [
    path('', MainPage.as_view(), name='main_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
