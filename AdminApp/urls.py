from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [

    path('',views.hello,name="hello"),
    path('catinfo',views.catinfo,name='catinfo'),
    path('table',views.table,name='table'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('catform',views.catform,name='catform'),
   
    path('productinfo',views.productinfo,name='productinfo'),
    path('table1',views.table1,name='table1'),
    path('delete1/<int:id>',views.delete1,name='delete1'),
    path('edit1/<int:id>',views.edit1,name='edit1'),
    path('update1/<int:id>',views.update1,name='update1'),
    path('productform',views.productform,name='productform'),

    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
    path('reguser',views.reguser,name='reguser'),

    path('usertable',views.usertable,name='usertable'),
    

    ]