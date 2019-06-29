from django import forms
from webapp.models import Author, Book


class AuthorCreateForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                      'placeholder': 'Дата рождения'}))

    death_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                      'placeholder': 'Дата смерти'}))

    photography = forms.ImageField(
        widget=forms.FileInput(attrs={'type': "file", 'class': 'form-control-file',
                                         'placeholder': 'Фотография'}), required=False)

    class Meta:
        model = Author
        fields = ['full_name', 'birth_date', 'death_date', 'biography', 'photography']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                                'placeholder': 'ФИО Автора'}),


            'biography': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Биография'}),

        }


class AuthorUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                        'placeholder': 'Дата рождения'}))

    death_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                      'placeholder': 'Дата смерти'}))

    photography = forms.ImageField(
        widget=forms.FileInput(attrs={'type': "file", 'class': 'form-control-file',
                                      'placeholder': 'Фотография'}), required=False)

    class Meta:
        model = Author
        fields = ['full_name', 'birth_date', 'death_date', 'biography', 'photography']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                                'placeholder': 'ФИО Автора'}),



            'biography': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Биография'}),


        }


class BookCreateForm(forms.ModelForm):
    published_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                      'placeholder': 'Год издания'}))

    author = forms.ModelChoiceField(queryset=Author.objects.active(),
                                            widget=forms.Select
                                            (attrs={'class': 'form-control form-control-sm shadow-none'}),
                                            required=True)

    class Meta:
        model = Book
        fields = ['name', 'author', 'published_date', 'file', 'cover', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Описание книги'}),

            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Название книги'}),
        }


class BookUpdateForm(forms.ModelForm):
    published_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                      'placeholder': 'Год издания'}))

    author = forms.ModelChoiceField(queryset=Author.objects.active(),
                                            widget=forms.Select
                                            (attrs={'class': 'form-control form-control-sm shadow-none'}),
                                            required=True)

    class Meta:
        model = Book
        fields = ['name', 'author', 'published_date', 'file', 'cover', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Описание книги'}),

            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Название книги'}),
        }