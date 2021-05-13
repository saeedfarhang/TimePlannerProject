from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class StartEndTimeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    timeinsecond = models.IntegerField(default=0)
    def __str__(self):
        return str(self.start_time) +' | ' + str(self.end_time) 
    
    def get_second(self):
        diffrence_time = self.end_time - self.start_time
        self.timeinsecond = diffrence_time.total_seconds()
    



class TimeTrackRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(null=True, blank=True)
    start_end_records = models.ManyToManyField('timetracker.StartEndTimeRecord', blank=True)

    def __str__(self):
        return self.title

    def get_time_in_second(self):
        self.save()
