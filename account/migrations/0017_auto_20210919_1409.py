# Generated by Django 3.2.4 on 2021-09-19 10:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0016_auto_20210917_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=255, verbose_name='Olke'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Adi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='dostlar', to=settings.AUTH_USER_MODEL, verbose_name='Dostlar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Gen', 'Kisi'), ('Gen', 'Kadin'), ('Gen', 'Yeniyetme')], max_length=255, null=True, verbose_name='Cinsiyyet'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Soyad'),
        ),
    ]