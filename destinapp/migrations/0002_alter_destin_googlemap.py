# Generated by Django 5.0.6 on 2024-08-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destin',
            name='GoogleMap',
            field=models.URLField(max_length=800),
        ),
    ]
