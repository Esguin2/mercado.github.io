# Generated by Django 4.2.1 on 2023-06-23 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cedula', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('nombreCompleto', models.TextField(max_length=30)),
                ('dirrecion', models.TextField(max_length=30)),
                ('telefono', models.TextField(max_length=30)),
                ('correo', models.TextField(max_length=30)),
            ],
        ),
    ]
