# Generated by Django 4.1.5 on 2023-01-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('director', models.CharField(max_length=200)),
                ('actors', models.TextField()),
                ('producer', models.CharField(max_length=200)),
                ('production_date', models.DateTimeField()),
                ('release_date', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('pulish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
