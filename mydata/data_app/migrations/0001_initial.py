# Generated by Django 4.2.5 on 2023-09-18 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='Activity Category')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=255, verbose_name='Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_one', models.CharField(max_length=255, verbose_name='Employee One')),
            ],
        ),
        migrations.CreateModel(
            name='EndPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chainage', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='End Point Chainage')),
                ('location', models.CharField(max_length=255, verbose_name='Share Location')),
                ('photo', models.ImageField(upload_to='end_point_photos/', verbose_name='Share End Point Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=255, verbose_name='Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='MyDateForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_date', models.DateField(verbose_name='My Date')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255, verbose_name='Site')),
            ],
        ),
        migrations.CreateModel(
            name='StartPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chainage', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Start Point Chainage')),
                ('location', models.CharField(max_length=255, verbose_name='Share Location')),
                ('photo', models.ImageField(upload_to='start_point_photos/', verbose_name='Share Start Point Photo')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, verbose_name='Activity Type')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_app.activitycategory')),
            ],
        ),
    ]
