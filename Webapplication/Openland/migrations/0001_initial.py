# Generated by Django 4.1.3 on 2022-11-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='User name')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('cpass', models.CharField(max_length=20, verbose_name='Confirm password')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=20, verbose_name='Owner Name')),
                ('price', models.CharField(default='', max_length=20, verbose_name='Price')),
                ('address', models.CharField(default='', max_length=100, verbose_name='Location')),
                ('about', models.TextField(default='', max_length=200, verbose_name='Description')),
                ('phone_no', models.CharField(default='', max_length=10, verbose_name='Phone number')),
            ],
        ),
    ]
