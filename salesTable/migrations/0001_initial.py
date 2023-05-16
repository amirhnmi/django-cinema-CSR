# Generated by Django 4.2 on 2023-05-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='salestable')),
                ('price', models.IntegerField()),
                ('last_update', models.DateTimeField()),
            ],
        ),
    ]
