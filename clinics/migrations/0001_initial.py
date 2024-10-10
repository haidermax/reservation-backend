# Generated by Django 5.1.1 on 2024-10-10 18:44

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BeautyCenter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('center_name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('availability_time', models.CharField(max_length=255)),
                ('gps_location', models.CharField(blank=True, max_length=255, null=True)),
                ('advertise', models.BooleanField(default=False)),
                ('advertise_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('advertise_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beauty_centers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('hospital_name', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=255)),
                ('administration', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('availability_time', models.CharField(max_length=255)),
                ('gps_location', models.CharField(blank=True, max_length=255, null=True)),
                ('advertise', models.BooleanField(default=False)),
                ('advertise_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('advertise_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospitals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('laboratory_name', models.CharField(max_length=255)),
                ('available_tests', models.TextField()),
                ('bio', models.TextField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('availability_time', models.CharField(max_length=255)),
                ('gps_location', models.CharField(blank=True, max_length=255, null=True)),
                ('advertise', models.BooleanField(default=False)),
                ('advertise_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('advertise_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='laboratories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalCenter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('center_name', models.CharField(max_length=255)),
                ('director_name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('availability_time', models.CharField(max_length=255)),
                ('gps_location', models.CharField(blank=True, max_length=255, null=True)),
                ('advertise', models.BooleanField(default=False)),
                ('advertise_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('advertise_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medical_centers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('clinic_name', models.CharField(max_length=255)),
                ('working_hours', models.CharField(max_length=255)),
                ('gps_location', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clinics', to='doctors.doctor')),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s_records', to=settings.AUTH_USER_MODEL)),
                ('medical_center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clinics', to='clinics.medicalcenter')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
