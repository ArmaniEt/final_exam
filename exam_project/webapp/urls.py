from django.urls import path
from webapp.views import MainPage
app_name = 'webapp'


urlpatterns = [
    path('', MainPage.as_view(), name='main_page')
]