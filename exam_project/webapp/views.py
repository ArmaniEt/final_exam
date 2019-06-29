from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from webapp.forms import AuthorCreateForm, AuthorUpdateForm
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from webapp.models import Author


class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'main.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author_create.html'

    def get_success_url(self):
        return reverse('webapp:author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorUpdateForm
    template_name = 'author_update.html'

    def get_success_url(self):
        return reverse('webapp:author_list')

