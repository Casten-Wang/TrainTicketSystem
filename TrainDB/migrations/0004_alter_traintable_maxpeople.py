# Generated by Django 3.2.9 on 2021-12-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrainDB', '0003_alter_traintable_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traintable',
            name='maxpeople',
            field=models.IntegerField(default=20),
        ),
    ]
