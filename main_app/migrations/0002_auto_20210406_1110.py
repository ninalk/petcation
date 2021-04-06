# Generated by Django 3.1.7 on 2021-04-06 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='pet_pic',
        ),
        migrations.AddField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.owner'),
            preserve_default=False,
        ),
    ]
