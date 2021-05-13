# Generated by Django 3.2.2 on 2021-05-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0002_auto_20210511_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartEndTimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='timetrackrecord',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='timetrackrecord',
            name='start_time',
        ),
        migrations.AddField(
            model_name='timetrackrecord',
            name='start_end_records',
            field=models.ManyToManyField(to='timetracker.StartEndTimeRecord'),
        ),
    ]