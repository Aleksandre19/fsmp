# Generated by Django 3.1.6 on 2021-06-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_auto_20210603_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='offering',
            field=models.BooleanField(default=False),
        ),
    ]
