# Generated by Django 2.0.5 on 2018-09-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static_proj/images/noimage.png', null=True, upload_to='images_uploaded/'),
        ),
    ]