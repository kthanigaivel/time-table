import os
import django

import time

 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projext.settings')
django.setup()

from scheduler.models import *

def timer():
    Time = time.strftime('%H:%M:%S')

    orderbyList = ['period_end', 'period_duration', 'count']
    sch=Schedule.objects.filter(is_the_chosen_one=True)
    tt=TimeTable.objects.all().order_by(*orderbyList).filter(schedule_id=sch.get().id)
    alarm=[]
    for x in tt.values():
        print(x['period_end'])
        
        alarm.append(x['period_end'])


        
 

timer()