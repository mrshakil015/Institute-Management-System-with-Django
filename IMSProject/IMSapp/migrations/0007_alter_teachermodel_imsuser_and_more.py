# Generated by Django 5.0.6 on 2024-06-26 17:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSapp', '0006_alter_teachermodel_imsuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='Imsuser',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacherinfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='websitecontactmodel',
            name='Imsuser',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
