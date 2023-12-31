# Generated by Django 4.2.3 on 2023-10-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='event_images/')),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExecutiveBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image_url', models.URLField()),
                ('level', models.IntegerField()),
                ('role', models.CharField(choices=[('Chair', 'Chair'), ('Vice Chair', 'Vice Chair'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer')], max_length=50)),
                ('description', models.TextField()),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image_url', models.URLField()),
                ('level', models.IntegerField()),
                ('description', models.TextField()),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image_url', models.URLField()),
                ('level', models.IntegerField()),
                ('role', models.CharField(choices=[('Program Committee', 'Program Committee'), ('Publicity Committee', 'Publicity Committee'), ('Membership Committee', 'Membership Committee'), ('Nominating Committee', 'Nominating Committee'), ('Social Media Committee', 'Social Media Committee'), ('Assistant Committee', 'Assistant Committee'), ('Volunteers and Regular Branch members', 'Volunteers and Regular Branch members')], max_length=50)),
                ('description', models.TextField()),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
