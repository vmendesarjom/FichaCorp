# Generated by Django 2.0.7 on 2018-10-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0002_auto_20181003_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='classe',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='equipamento',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='raca',
            field=models.CharField(max_length=20),
        ),
    ]
