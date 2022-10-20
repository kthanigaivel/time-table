from django.shortcuts import get_object_or_404, redirect, render

from . models import *
from . forms import TimeTableForm,ScheduleForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import time


def timer(request):
    orderbyList = ['period_end', 'period_duration', 'count']
    sch=Schedule.objects.filter(is_the_chosen_one=True)
    tt=TimeTable.objects.all().order_by(*orderbyList).filter(schedule_id=sch.get().id)
    print(tt.values())
    return HttpResponse("OK")

def index(request):
    context={}
    sch=Schedule.objects.all()

    if request.method=="POST":
        obj = get_object_or_404(Schedule,id= request.POST['item_id'])
        obj.is_the_chosen_one = True
        obj.save()

        print(request.POST['item_id'])

        messages.success(request,"Schedule Selected Successfully !")
    
    context={}
    context['form']=sch
    

    return render (request,'scheduler/dash.html',context)


def tables(request):
    context={}

    try:
        sch=Schedule.objects.filter(is_the_chosen_one=True)
        tt=TimeTable.objects.all().filter(schedule_id=sch.get().id)
        context['timetable'] =  tt
        context['sch'] = sch
    except:
        print("error")

    
    return render (request,'scheduler/tables.html',context)


def delete(request,id):
    context={}
    obj = get_object_or_404(TimeTable,id= id)
    form = TimeTableForm(request.POST or None,instance=obj)
    if request.method=="POST":
        obj.delete()
        messages.error(request,"%s Deleted Successfully !" % obj.name)
        return redirect("/tt/tables")
  
    context['form']= form
     
    return render (request,'scheduler/delete.html',context)


def update(request,id):
    context={}
    obj = get_object_or_404(TimeTable,id= id)
    form = TimeTableForm(request.POST or None,instance=obj)
    print(form.validate_unique)
    if form.is_valid():
        obj.delete()
        #form.save()
        timetable,craeted=TimeTable.objects.get_or_create(**form.cleaned_data)
        print(timetable)
        print(craeted)
        

        if craeted:
            messages.warning(request, "%s Updated Successfully !" % timetable )
        else:
            messages.error(request,"Not Updated !")
        return redirect("/tt/tables")
    context['form']= form
     
    return render (request,'scheduler/update.html',context)

def create(request):
    form = TimeTableForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        timetable,craeted=TimeTable.objects.get_or_create(**form.cleaned_data)
        #form.save()
        messages.success(request,"Saved Successfully !")
        return redirect("/tt/tables")
 
    context={}
    context['form']= form

    return render (request,'scheduler/create.html',context)