# Generated by Django 4.2.5 on 2023-09-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='media_files/')),
            ],
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='chainage',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='end_point_photos/'),
        ),
        migrations.AlterField(
            model_name='startpoint',
            name='chainage',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='startpoint',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='startpoint',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='start_point_photos/'),
        ),
    ]
