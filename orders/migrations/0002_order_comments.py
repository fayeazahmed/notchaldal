# Generated by Django 3.1.4 on 2020-12-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
