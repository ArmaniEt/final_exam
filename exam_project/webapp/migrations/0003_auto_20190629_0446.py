# Generated by Django 2.2.2 on 2019-06-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190629_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photography',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]