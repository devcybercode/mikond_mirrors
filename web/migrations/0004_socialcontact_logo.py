# Generated by Django 5.1.3 on 2024-12-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_socialcontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialcontact',
            name='logo',
            field=models.ImageField(default='none', upload_to='logo/%Y/%m/%d/'),
        ),
    ]
