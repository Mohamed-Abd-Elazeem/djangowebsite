# Generated by Django 4.2.11 on 2024-04-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='getintouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('phonenumber', models.TextField(max_length=30)),
                ('email', models.TextField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
    ]
