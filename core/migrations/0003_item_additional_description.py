# Generated by Django 3.1.7 on 2021-06-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210607_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='additional_description',
            field=models.TextField(default='Sth'),
            preserve_default=False,
        ),
    ]