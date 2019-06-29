from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from webapp.models import Author


class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'main.html'


class AuthorListView(ListView):
    model = Author
