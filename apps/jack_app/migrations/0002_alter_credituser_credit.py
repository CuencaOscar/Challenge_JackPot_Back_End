# Generated by Django 3.2.6 on 2022-02-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jack_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credituser',
            name='credit',
            field=models.SmallIntegerField(default=10),
        ),
    ]