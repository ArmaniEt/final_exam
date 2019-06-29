from django.db import models


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class Author(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО автора")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    death_date = models.DateField(null=True, blank=True, verbose_name="Дата смерти")
    biography = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Биография")
    photography = models.ImageField(upload_to='images/', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return "%s" % self.full_name

# Book model


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books', verbose_name='Автор')
    published_date = models.CharField(max_length=255, verbose_name="Год издания")
    file = models.FileField(upload_to='texts/', null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
