# Generated by Django 3.1.7 on 2021-04-06 17:55

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
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=600)),
                ('pets', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=600)),
                ('sit_count', models.IntegerField(null=True)),
                ('pet_experience', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('details', models.TextField(max_length=600)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('pet_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.owner')),
                ('sitter_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.sitter')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pet_type', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('characteristics', models.TextField(max_length=400)),
                ('care_instructions', models.TextField(max_length=600)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.owner')),
            ],
        ),
    ]
