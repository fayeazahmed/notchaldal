# Generated by Django 3.1.4 on 2020-12-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201223_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
