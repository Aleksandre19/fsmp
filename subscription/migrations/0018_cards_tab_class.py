# Generated by Django 3.1.6 on 2021-08-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0017_auto_20210810_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='tab_class',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
