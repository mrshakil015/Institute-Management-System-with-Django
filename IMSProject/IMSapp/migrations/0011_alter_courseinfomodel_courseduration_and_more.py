# Generated by Django 5.0.6 on 2024-06-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSapp', '0010_alter_courseinfomodel_classduration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfomodel',
            name='CourseDuration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='courseinfomodel',
            name='CourseFee',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='courseinfomodel',
            name='Lecture',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='courseinfomodel',
            name='TotalProject',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='courseinfomodel',
            name='WeeklyClass',
            field=models.IntegerField(null=True),
        ),
    ]
