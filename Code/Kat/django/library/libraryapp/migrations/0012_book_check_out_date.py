# Generated by Django 2.2 on 2019-04-23 21:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0011_book_checked_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='check_out_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
