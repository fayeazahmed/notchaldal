# Generated by Django 3.1.4 on 2020-12-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201224_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='successful_orders',
            field=models.IntegerField(default=0),
        ),
    ]