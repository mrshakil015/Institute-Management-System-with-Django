# Generated by Django 5.0.6 on 2024-06-27 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMSapp', '0006_alter_admittedcoursemodel_learningbatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admittedcoursemodel',
            name='LearningBatch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IMSapp.batchinfomodel'),
        ),
    ]
