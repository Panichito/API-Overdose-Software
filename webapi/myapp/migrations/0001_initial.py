# Generated by Django 4.1.3 on 2022-11-04 08:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alert_time', models.TimeField(blank=True, null=True)),
                ('Alert_isTake', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Caretaker_since', models.DateField(default=datetime.date.today)),
                ('Caretaker_status', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicine_name', models.CharField(max_length=100)),
                ('Medicine_type', models.CharField(choices=[('Liquid', 'Liquid'), ('Tablet', 'Tablet'), ('Capsules', 'Capsules')], max_length=50)),
                ('Medicine_info', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_usertype', models.CharField(choices=[('PATIENT', 'PATIENT'), ('CARETAKER', 'CARETAKER'), ('ADMIN', 'ADMIN')], default='PATIENT', max_length=16)),
                ('Member_birthdate', models.DateField()),
                ('Member_gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=8)),
                ('Member_token', models.CharField(default='-', max_length=100)),
                ('Member_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caretaker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.caretaker')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_disease', models.CharField(max_length=100)),
                ('Record_amount', models.IntegerField(default=0)),
                ('Record_start', models.DateField(default=datetime.date.today)),
                ('Record_end', models.DateField(blank=True, null=True)),
                ('Record_info', models.TextField(blank=True, null=True)),
                ('Record_isComplete', models.BooleanField(default=False)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.medicine')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('History_takeTime', models.DateTimeField(blank=True, null=True)),
                ('alert', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.alert')),
            ],
        ),
        migrations.AddField(
            model_name='caretaker',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.member'),
        ),
        migrations.AddField(
            model_name='alert',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.record'),
        ),
    ]
