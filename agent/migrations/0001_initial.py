# Generated by Django 4.0 on 2021-12-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao1', models.CharField(max_length=200)),
                ('descricao2', models.CharField(max_length=200)),
                ('descricao3', models.CharField(max_length=200)),
                ('servicos1', models.CharField(max_length=100)),
                ('servicos2', models.CharField(max_length=100)),
                ('servicos3', models.CharField(max_length=100)),
            ],
        ),
    ]
