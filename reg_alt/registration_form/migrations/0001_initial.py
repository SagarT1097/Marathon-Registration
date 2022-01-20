# Generated by Django 2.0.7 on 2018-07-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phno', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=100, null=True)),
                ('emailid', models.EmailField(max_length=50, null=True)),
                ('gender', models.CharField(choices=[('m', 'MALE'), ('f', 'FEMALE'), ('o', 'OTHERS')], default='Male', max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('teesize', models.CharField(max_length=200, null=True)),
                ('prevruns', models.IntegerField(blank=True, null=True)),
                ('bibno', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
