# Generated by Django 3.1.6 on 2021-05-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_subjects_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='liked',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
