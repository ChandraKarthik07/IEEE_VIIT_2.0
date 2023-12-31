# Generated by Django 4.2.3 on 2023-10-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event_executivebody_faculty_operatingbody'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executivebody',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='operatingbody',
            name='image_url',
        ),
        migrations.AddField(
            model_name='executivebody',
            name='image',
            field=models.ImageField(default='profiles/default.jpg', upload_to='profiles/'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(default='profiles/default.jpg', upload_to='profiles/'),
        ),
        migrations.AddField(
            model_name='operatingbody',
            name='image',
            field=models.ImageField(default='profiles/default.jpg', upload_to='profiles/'),
        ),
    ]
