from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import AuthorCreateForm, AuthorUpdateForm, BookCreateForm, BookUpdateForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.models import Author, Book
from django.contrib.auth.decorators import login_required


class BookListView(ListView):
    model = Book
    template_name = 'main.html'


class AuthorListView(ListView):
    queryset = Author.objects.active()
    model = Author
    template_name = 'author_list.html'


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author_create.html'

    def get_success_url(self):
        return reverse('webapp:author_list')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorUpdateForm
    template_name = 'author_update.html'

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


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'book_create.html'

    def get_success_url(self):
        return reverse('webapp:main_page')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookUpdateForm
    template_name = 'book_update.html'

    def get_success_url(self):
        return reverse('webapp:main_page')


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    permission_required = 'webapp.book_delete'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.has_permission():
    #         return redirect('webapp:author_list')
    #     return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:main_page')
