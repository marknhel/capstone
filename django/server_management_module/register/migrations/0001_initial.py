# Generated by Django 3.2.12 on 2022-05-05 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(max_length=50)),
                ('mac_address', models.CharField(max_length=50)),
                ('blocked', models.BooleanField(default=False)),
                ('profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='register.profile')),
            ],
        ),
    ]
