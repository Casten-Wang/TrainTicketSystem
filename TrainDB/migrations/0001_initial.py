# Generated by Django 3.2.9 on 2021-11-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainnum', models.CharField(max_length=10)),
                ('maxpeople', models.IntegerField()),
                ('begintime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('origin', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=10)),
                ('firstclassprice', models.FloatField()),
                ('secondclassprice', models.FloatField()),
            ],
        ),
    ]
