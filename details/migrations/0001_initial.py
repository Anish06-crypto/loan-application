# Generated by Django 3.2.5 on 2021-07-19 07:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=6)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\d{10,10}$')])),
                ('email', models.EmailField(max_length=254)),
                ('marital_status', models.CharField(choices=[('Married', 'married'), ('Unmarried', 'unmarried'), ('Separated', 'separated')], max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('state', models.CharField(choices=[('Karnataka', 'karnataka'), ('Maharashtra', 'maharashtra'), ('New York', 'new york'), ('Texas', 'texas'), ('Melbourne', 'melbourne')], max_length=30)),
                ('pin_code', models.CharField(blank=True, max_length=6, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\d{6,6}$')])),
                ('country', models.CharField(choices=[('India', 'India'), ('USA', 'USA'), ('Australia', 'Australia')], max_length=30)),
                ('mailing_address', models.CharField(choices=[('T', 'True'), ('F', 'False')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DependantDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('borrower_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='CoBorrowerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_borrower_name', models.CharField(max_length=100)),
                ('cob_age', models.IntegerField()),
                ('annual_income', models.IntegerField()),
                ('borrower_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.personaldetails')),
            ],
        ),
    ]
