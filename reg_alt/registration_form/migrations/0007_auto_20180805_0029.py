# Generated by Django 2.0.7 on 2018-08-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_form', '0006_auto_20180804_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='finish',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='split',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='start',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
