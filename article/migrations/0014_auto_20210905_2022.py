# Generated by Django 3.2.4 on 2021-09-05 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_alter_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug_alani',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='slug_alani',
            new_name='slug',
        ),
    ]
