# Generated by Django 3.2.4 on 2021-08-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='oxudugu_yer',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
