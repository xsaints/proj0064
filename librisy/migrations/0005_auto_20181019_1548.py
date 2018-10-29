# Generated by Django 2.1.2 on 2018-10-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librisy', '0004_auto_20181019_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN'),
        ),
    ]
