# Generated by Django 3.2.4 on 2021-09-16 04:56

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20210904_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelManagers(
            name='relationship',
            managers=[
                ('data', django.db.models.manager.Manager()),
            ],
        ),
    ]
