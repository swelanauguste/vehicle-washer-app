# Generated by Django 4.2.6 on 2023-10-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='vehicles/photos')),
                ('plate', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=25, max_digits=4)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
    ]