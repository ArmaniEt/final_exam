# Generated by Django 2.2.2 on 2019-06-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя автора')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Дата смерти')),
                ('biography', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Биография')),
                ('photography', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
