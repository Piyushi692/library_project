# Generated by Django 4.2.6 on 2024-01-23 16:41

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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(upload_to='authors/')),
                ('author_id', models.CharField(max_length=15, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('cover_image', models.ImageField(upload_to='books/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.genre')),
            ],
        ),
    ]
