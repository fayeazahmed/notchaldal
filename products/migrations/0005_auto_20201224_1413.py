# Generated by Django 3.1.4 on 2020-12-24 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201224_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='product images/'),
        ),
    ]
