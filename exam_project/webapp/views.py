from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import AuthorCreateForm, AuthorUpdateForm, BookCreateForm, BookUpdateForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from webapp.models import Author, Book
from django.contrib.auth.decorators import login_required


class BookListView(ListView):
    model = Book
    template_name = 'main.html'


class AuthorListView(ListView):
    queryset = Author.objects.active()
    model = Author
    template_name = 'author_list.html'


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author_create.html'
    permission_required = 'webapp.add_author'

    def get_success_url(self):
        return reverse('webapp:author_list')


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorUpdateForm
    template_name = 'author_update.html'
    permission_required = 'webapp.change_author'

    def get_success_url(self):
        return reverse('webapp:author_list')


@login_required
def soft_delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.is_deleted = True
    author.save()
    return redirect('webapp:author_list')


def book_download(request, pk):
    book = get_object_or_404(Book, pk=pk)
    file = book.file
    file_name = book.file.name
    response = HttpResponse(file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name

    return response


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'book_create.html'
    permission_required = 'webapp.add_book'

    def get_success_url(self):
        return reverse('webapp:main_page')


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookUpdateForm
    template_name = 'book_update.html'
    permission_required = 'webapp.change_book'

    def get_success_url(self):
        return reverse('webapp:main_page')


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    permission_required = 'webapp.delete_book'

    def get_success_url(self):
        return reverse('webapp:main_page')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
