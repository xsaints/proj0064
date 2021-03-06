# Generated by Django 2.1.2 on 2018-10-18 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('udemyx', '0003_auto_20181012_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=models.CharField(db_index=True, max_length=500), max_length=500),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='udemyx.Category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(db_index=True, max_length=500),
        ),
        migrations.AlterIndexTogether(
            name='course',
            index_together={('title', 'slug')},
        ),
    ]
