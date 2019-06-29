from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render
from webapp.forms import AuthorCreateForm
from django.views.generic import ListView, TemplateView, CreateView
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
