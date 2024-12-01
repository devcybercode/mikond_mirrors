# Generated by Django 5.1.3 on 2024-11-25 15:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_mirrors'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField()),
                ('telegram', models.URLField()),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9981234567'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'verbose_name': 'Social Contact',
                'verbose_name_plural': 'Social Contacts',
                'ordering': ('-id',),
            },
        ),
    ]
