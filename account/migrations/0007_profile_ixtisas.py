# Generated by Django 3.2.4 on 2021-08-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_profile_oxudugu_yer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ixtisas',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
