# Generated by Django 3.1.6 on 2021-05-11 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_auto_20210510_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='category_id',
            new_name='category',
        ),
    ]
