# Generated by Django 2.2 on 2019-04-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbooking',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='userbooking',
            name='start_date',
            field=models.DateField(),
        ),
    ]
