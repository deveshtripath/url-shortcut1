# Generated by Django 3.2.6 on 2021-08-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0005_auto_20200830_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
