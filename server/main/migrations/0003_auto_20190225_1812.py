# Generated by Django 2.1.5 on 2019-02-25 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20190225_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/bikes/')),
                ('number', models.CharField(default='https://', max_length=10)),
                ('helmet', models.BooleanField(default=True)),
                ('gf_lat', models.DecimalField(decimal_places=10, max_digits=16)),
                ('gf_lon', models.DecimalField(decimal_places=10, max_digits=16)),
                ('gf', models.BooleanField(default=True)),
                ('gf_limit', models.IntegerField(default=10)),
                ('speed', models.BooleanField(default=True)),
                ('speed_limit', models.IntegerField(default=60)),
                ('token', models.CharField(max_length=40)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BikeAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Bike')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BikeAccessRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Bike')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BikeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF'), ('EMERGENCY', 'EMERGENCY'), ('LOST', 'LOST')], max_length=10)),
                ('current_lat', models.DecimalField(decimal_places=10, max_digits=16)),
                ('current_lon', models.DecimalField(decimal_places=10, max_digits=16)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Bike')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RideSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_coordinates', models.TextField()),
                ('avg_speed', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('helmet', models.BooleanField(default=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Bike')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/bikes/'),
        ),
    ]
