# Generated by Django 2.2.2 on 2019-06-29 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0005_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersBookShelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ManyToManyField(related_name='book_on_shelf', to='webapp.Book', verbose_name='Книга на полке')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='book_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
