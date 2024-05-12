# Generated by Django 5.0.6 on 2024-05-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=100, verbose_name='آدرس الکترونیکی')),
                ('phone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('number', models.IntegerField(default=1, verbose_name='تعداد')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('time', models.DateField(verbose_name='ساعت')),
            ],
        ),
    ]