# Generated by Django 3.2.4 on 2021-09-06 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_alter_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='hit_post',
            new_name='hit',
        ),
    ]