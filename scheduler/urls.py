from django.urls import path
from .  import views

urlpatterns=[
    path('create', views.create ),
    path('edit/<int:id>', views.update ),
    path('delete/<int:id>', views.delete ),
    path('',views.index,name='index'),
    path('tables/',views.tables,name='index'),
    path('timer/',views.timer,name='timer'),


]