# Generated by Django 4.0.3 on 2022-03-12 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('height', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images/')),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_generated', models.BooleanField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('collections', models.ManyToManyField(to='api.collection')),
                ('images', models.ManyToManyField(to='api.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Набор',
                'verbose_name_plural': 'Наборы',
            },
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.collection')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.image')),
            ],
            options={
                'verbose_name': 'Слой',
                'verbose_name_plural': 'Слои',
            },
        ),
    ]
