# Generated by Django 4.1 on 2022-10-04 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInformation',
            fields=[
                ('app_name', models.CharField(default='oidc', max_length=32, primary_key=True, serialize=False)),
                ('client_id', models.CharField(max_length=128)),
                ('client_secret', models.CharField(max_length=256)),
            ],
        ),
    ]
