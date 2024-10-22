# Generated by Django 5.0.6 on 2024-06-19 16:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('biography', models.CharField(max_length=3000)),
                ('image_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('duty_type', models.CharField(choices=[('1', 'Crew'), ('2', 'Cast'), ('3', 'Director'), ('4', 'Writer')], max_length=50)),
                ('contact', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(20)])),
                ('image_name', models.CharField(max_length=50)),
                ('image_cover', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('slug', models.SlugField(unique=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=19)),
                ('language', models.CharField(max_length=100)),
                ('genres', models.ManyToManyField(to='movies.genre')),
                ('people', models.ManyToManyField(to='movies.person')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
