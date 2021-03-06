# Generated by Django 3.2.4 on 2021-08-27 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_created_at_profile_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Send', 'Send'), ('Accepted', 'Accepted')], max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reciver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciver', to='account.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='account.profile')),
            ],
        ),
    ]
