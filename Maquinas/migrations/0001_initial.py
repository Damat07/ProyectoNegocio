# Generated by Django 4.1 on 2022-09-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=40)),
                ('año', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
    ]
