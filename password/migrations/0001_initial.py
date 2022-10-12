# Generated by Django 4.1.1 on 2022-10-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.CharField(max_length=255)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('url', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255)),
            ],
        ),
    ]
