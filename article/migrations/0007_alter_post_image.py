# Generated by Django 3.2.4 on 2021-09-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='users'),
        ),
    ]
