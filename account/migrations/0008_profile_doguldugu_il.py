# Generated by Django 3.2.4 on 2021-08-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_profile_ixtisas'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='doguldugu_il',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
