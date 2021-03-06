# Generated by Django 2.2.2 on 2019-06-29 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_author_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название книги')),
                ('published_date', models.CharField(max_length=255, verbose_name='Год издания')),
                ('file', models.FileField(blank=True, null=True, upload_to='texts/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='webapp.Author', verbose_name='Автор')),
            ],
        ),
    ]
