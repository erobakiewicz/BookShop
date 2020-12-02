# Generated by Django 3.1.2 on 2020-12-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookies', '0008_auto_20201202_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
