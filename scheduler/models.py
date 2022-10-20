from enum import unique
from django.db import models
from django.db import transaction
from datetime import datetime, date

from django.forms import DurationField

class Schedule(models.Model):
        # fields of the model
    schedule = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "images/")
    is_the_chosen_one = models.BooleanField()



   
    def save(self, *args, **kwargs):
        if not self.is_the_chosen_one:
            return super(Schedule, self).save(*args, **kwargs)
        with transaction.atomic():
            Schedule.objects.filter(
                is_the_chosen_one=True).update(is_the_chosen_one=False)
            return super(Schedule, self).save(*args, **kwargs)
 
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.schedule


class TimeTable(models.Model):
    schedule = models.ForeignKey(Schedule,on_delete= models.CASCADE)
    name = models.CharField(max_length = 20 )
    period_start = models.TimeField()
    period_end= models.TimeField()

    period_duration = models.DurationField(blank=True)
    count = models.PositiveIntegerField()
    bell_duration = models.DurationField(max_length=2)


    def save(self, *args, **kwargs):
        dur=datetime.combine(date.today(),  self.period_end) - datetime.combine(date.today(), self.period_start)
        with transaction.atomic():
            self.period_duration = dur
            return super(TimeTable, self).save(*args, **kwargs)
            
  
    def __str__(self):
        return self.name
