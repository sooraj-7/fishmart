from django.shortcuts import render,redirect
from.models import*
from UserApp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def hello(request):
        cat=category.objects.all().count()
        prod=product.objects.all().count()
        ruser=register.objects.all().count()
        fback=feedback.objects.all().count()
        odr=cart.objects.all().count()
        return render(request,'admin.html',{'cat':cat,'prod':prod,'ruser':ruser,'fback':fback,'odr':odr})

def catinfo(request):
    if request.method =='POST':
        name=request.POST['name']
        image=request.FILES['image']
        data=category(name=name,image=image)
        data.save()
    return redirect('catform')

def table(request):
    data=category.objects.all()
    return render(request,'table.html',{'data':data})


def edit(request,id):
    data=category.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})

def delete(request,id):
    category.objects.filter(id=id).delete()
    return redirect('table')

def catform(request):
    return render(request,'category.html')

def update(request,id):
    if request.method =='POST':
        name=request.POST['name']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = category.objects.get(id=id).image

        category.objects.filter(id=id).update(name=name,image=file)
        return redirect('catinfo')




def productform(request):
    data=category.objects.all()
    return render(request,'product.html',{'data':data})


def productinfo(request):
    if request.method =='POST':
        name1=request.POST['name1']
        description1=request.POST['description1']
        price1=request.POST['price1']
        image1=request.FILES['image1']
        categories=request.POST['categories']
        data1=product(name1=name1,description1=description1,price1=price1,categories=categories,image1=image1)
        data1.save()
    return redirect('productform')

def table1(request):
    data1=product.objects.all()
    return render(request,'table1.html',{'data1':data1})


def edit1(request,id):
    data=category.objects.all()
    data1=product.objects.filter(id=id)
    return render(request,'edit1.html',{'data1':data1,'data':data})

def delete1(request,id):
    product.objects.filter(id=id).delete()
    return redirect('table1')


def update1(request,id):
    if request.method =='POST':
        name1=request.POST['name1']
        description1=request.POST['description1']
        price1=request.POST['price1']
        categories=request.POST['categories']
        try:
            img_c = request.FILES['image1']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = product.objects.get(id=id).image1

        product.objects.filter(id=id).update(name1=name1,description1=description1,price1=price1,categories=categories,image1=file)
        return redirect('productinfo')



def viewfeedback(request):
    data=feedback.objects.all()
    return render(request,'viewfeedback.html',{'data':data})

def reguser(request):
    data=register.objects.all()
    return render(request,'reguser.html',{'data':data})

def usertable(request):
    data1=cart.objects.all()
    return render(request,'tableuser.html',{'data1':data1})
