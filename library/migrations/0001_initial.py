# Generated by Django 2.1.1 on 2018-09-21 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=200)),
                ('publication_year', models.IntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Category')),
            ],
        ),
    ]
