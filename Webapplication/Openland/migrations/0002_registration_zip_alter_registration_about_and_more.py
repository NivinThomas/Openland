# Generated by Django 4.1.3 on 2022-11-19 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Openland', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='zip',
            field=models.CharField(default='', max_length=6, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='about',
            field=models.CharField(default='', max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
