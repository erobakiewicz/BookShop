# Generated by Django 3.1.2 on 2020-12-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookies', '0007_auto_20201202_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
