# Generated by Django 5.0.6 on 2024-07-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSapp', '0027_alter_teacherattendance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherattendance',
            name='Date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='teacherattendance',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
