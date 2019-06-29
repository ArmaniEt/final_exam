from django import forms
from webapp.models import Author


class AuthorCreateForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                      'placeholder': 'Дата рождения'}))

    death_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                      'placeholder': 'Дата смерти'}))

    photography = forms.ImageField(
        widget=forms.FileInput(attrs={'type': "file", 'class': 'form-control-file',
                                         'placeholder': 'Фотография'}))

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
                                      'placeholder': 'Фотография'}))

    class Meta:
        model = Author
        fields = ['full_name', 'birth_date', 'death_date', 'biography', 'photography']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                                'placeholder': 'ФИО Автора'}),



            'biography': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Биография'}),


        }
