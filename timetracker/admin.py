from django.contrib import admin
from .models import TimeTrackRecord, StartEndTimeRecord

admin.site.register(TimeTrackRecord)
admin.site.register(StartEndTimeRecord)