# Generated by Django 4.1.3 on 2022-12-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0007_alter_trees_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trees',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr-code'),
        ),
    ]
