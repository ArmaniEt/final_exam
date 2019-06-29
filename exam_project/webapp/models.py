from django.db import models

# Author model


class Author(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО автора")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    death_date = models.DateField(null=True, blank=True, verbose_name="Дата смерти")
    biography = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Биография")
    photography = models.ImageField(upload_to='images/', null=True, blank=True)

# Book model

