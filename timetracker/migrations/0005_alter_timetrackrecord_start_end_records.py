# Generated by Django 3.2.2 on 2021-05-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0004_alter_timetrackrecord_start_end_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetrackrecord',
            name='start_end_records',
            field=models.ManyToManyField(blank=True, to='timetracker.StartEndTimeRecord'),
        ),
    ]
