# Generated by Django 5.0.6 on 2024-06-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSapp', '0011_alter_courseinfomodel_courseduration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfomodel',
            name='CourseCategory',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='courseinfomodel',
            name='ShortSummary',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
