# Generated by Django 4.1.3 on 2023-02-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=250)),
                ('phone_number', models.CharField(blank=True, max_length=13)),
                ('address', models.TextField()),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'others')], max_length=1)),
                ('dob', models.DateField()),
                ('joining_date', models.DateField()),
                ('jobs', models.ManyToManyField(blank=True, to='emsapp.job')),
            ],
        ),
    ]
