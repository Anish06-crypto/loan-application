# Generated by Django 3.2.5 on 2021-07-19 08:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='aadhar_number',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="Aadhar number must be entered in the format: '1111 1111 1111 1111'. Up to 12 digits allowed.", regex='^\\d{12,12}$')]),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='pan_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Pan number must be entered in the format: 'AhsGr2783d'. Up to 10 digits allowed.", regex='^[A-Za-z]{5}\\d{4}[A-Za-z]{1}$')]),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='country',
            field=models.CharField(choices=[('India', 'India'), ('USA', 'USA'), ('Australia', 'Australia')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='mailing_address',
            field=models.CharField(choices=[('T', 'True'), ('F', 'False')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'married'), ('Unmarried', 'unmarried'), ('Separated', 'separated')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator(message="Pin number must be entered in the format: '99999'. Up to 6 digits allowed.", regex='^\\d{6,6}$')]),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='state',
            field=models.CharField(choices=[('Karnataka', 'karnataka'), ('Maharashtra', 'maharashtra'), ('New York', 'new york'), ('Texas', 'texas'), ('Melbourne', 'melbourne')], max_length=30, null=True),
        ),
    ]
