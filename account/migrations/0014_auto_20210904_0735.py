# Generated by Django 3.2.4 on 2021-09-04 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20210904_0720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='slugar',
            new_name='avatar',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='avatnds',
            new_name='friends',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='frie',
            new_name='slug',
        ),
    ]
