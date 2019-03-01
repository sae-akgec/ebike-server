# Generated by Django 2.1.5 on 2019-03-01 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20190227_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='bikeaccess',
            unique_together={('bike', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='bikeaccessrequest',
            unique_together={('bike', 'user')},
        ),
    ]
