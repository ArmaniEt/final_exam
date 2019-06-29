from django import forms
from webapp.models import Author


class AuthorCreateForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['full_name', 'birth_date', 'death_date', 'biography', 'photography']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                                'placeholder': 'ФИО Автора'}),

            # 'birth_date': forms.DateInput(
            #     format=('%d-%m-%Y'),
            #     attrs={'class': 'form-control form-control-sm shadow-none',
            #                                     'placeholder': 'Дата рождения'}),
            #
            # 'death_date': forms.DateInput(attrs={'class': 'form-control form-control-sm shadow-none',
            #                                      'placeholder': 'Дата смерти'}),

            'biography': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Биография'}),

            # 'photography': forms.ImageField(attrs={'class': 'form-control form-control-sm shadow-none',
            #                                      'placeholder': 'Фотография'}),

        }


class AuthorUpdateForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['full_name', 'birth_date', 'death_date', 'biography', 'photography']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                                'placeholder': 'ФИО Автора'}),

            # 'birth_date': forms.DateInput(
            #     format=('%d-%m-%Y'),
            #     attrs={'class': 'form-control form-control-sm shadow-none',
            #                                     'placeholder': 'Дата рождения'}),
            #
            # 'death_date': forms.DateInput(attrs={'class': 'form-control form-control-sm shadow-none',
            #                                      'placeholder': 'Дата смерти'}),

            'biography': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Биография'}),

            # 'photography': forms.ImageField(attrs={'class': 'form-control form-control-sm shadow-none',
            #                                      'placeholder': 'Фотография'}),

        }
