# Generated by Django 2.2 on 2019-04-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0010_remove_book_checked_outt'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='checked_out',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]