# Generated by Django 3.2.12 on 2022-03-25 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='server_id',
        ),
        migrations.DeleteModel(
            name='Server',
        ),
    ]