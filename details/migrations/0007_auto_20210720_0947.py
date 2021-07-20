# Generated by Django 3.2.5 on 2021-07-20 04:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_auto_20210720_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="Aadhar number must be entered in the format: '1111 1111 1111 1111'. Up to 12 digits allowed.", regex='^\\d{12,12}$')])),
                ('pan_number', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Pan number must be entered in the format: 'AhsGr2783d'. Up to 10 digits allowed.", regex='^[A-Za-z]{5}\\d{4}[A-Za-z]{1}$')])),
            ],
        ),
        migrations.RemoveField(
            model_name='moredetails',
            name='aadhar_number',
        ),
        migrations.RemoveField(
            model_name='moredetails',
            name='pan_number',
        ),
    ]