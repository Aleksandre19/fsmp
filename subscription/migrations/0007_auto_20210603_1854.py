# Generated by Django 3.1.6 on 2021-06-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0006_auto_20210603_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cards',
            name='saving',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
