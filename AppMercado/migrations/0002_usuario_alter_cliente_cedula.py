# Generated by Django 4.2.1 on 2023-06-26 23:52

import AppMercado.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMercado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('documento', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('usuario', models.TextField(default='valor_predeterminado', max_length=30)),
                ('password', models.CharField(max_length=255)),
                ('rol', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.TextField(max_length=20, primary_key=True, serialize=False, verbose_name=AppMercado.models.Usuario),
        ),
    ]
