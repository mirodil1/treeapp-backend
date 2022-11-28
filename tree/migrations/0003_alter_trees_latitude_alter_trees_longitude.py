# Generated by Django 4.1.3 on 2022-11-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_type_alter_trees_options_trees_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trees',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Kordinata'),
        ),
        migrations.AlterField(
            model_name='trees',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Kordinata'),
        ),
    ]