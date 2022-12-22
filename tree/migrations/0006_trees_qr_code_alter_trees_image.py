# Generated by Django 4.1.3 on 2022-12-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_alter_trees_latitude_alter_trees_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='trees',
            name='qr_code',
            field=models.ImageField(default='https://cdn.pixabay.com/photo/2014/12/22/00/07/tree-576847__480.png', upload_to='qr-code'),
        ),
        migrations.AlterField(
            model_name='trees',
            name='image',
            field=models.ImageField(blank=True, default='https://cdn.pixabay.com/photo/2014/12/22/00/07/tree-576847__480.png', upload_to='images'),
        ),
    ]
