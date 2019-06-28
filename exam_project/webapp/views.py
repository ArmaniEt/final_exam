from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'main.html'
