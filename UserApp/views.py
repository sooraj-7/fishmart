from django.shortcuts import render,redirect
from.models import*
from AdminApp.models import*
from django.db.models.aggregates import Sum

# Create your views here.
def user(request):
    data=category.objects.all()
    data1=product.objects.all()
    return render(request,"user.html",{'data':data,'data1':data1})

def about(request):
    data=category.objects.all()
    return render(request,"about.html",{'data':data})

def addcart(request,id):
    if request.method =='POST':
        user_id=request.session.get('u_id')
        quantity=request.POST.get('quantity')
        total=request.POST.get('total')
        data=cart(usercart=register.objects.get(id=user_id),userpro=product.objects.get(id=id),quantity=quantity,total=total)
        data.save()
    return redirect('addtocart')

def checkouts(request):
    data=cart.objects.all()
    return render(request,"checkout.html",{'data':data})

def checkoutdata(request):
    if request.method == "POST":
        checkoutid=request.session.get('u_id')
        address=request.POST.get('address')
        country=request.POST.get('country')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        data=cart.objects.filter(usercart=checkoutid,status=0)

        for i in data:
            data=checkout(usercheckout=register.objects.get(id=checkoutid),usercart=cart.objects.get(id=i.id),address=address,country=country,state=state,pincode=pincode)
            data.save()
            cart.objects.filter(id=i.id).update(status=1)
        return redirect('success')
    
def success(request):
    u_id=request.session.get('u_id')
    data=checkout.objects.filter(usercheckout=u_id)
    return render(request,'success.html',{'data':data})


def addtocart(request):
    user_id=request.session.get('u_id')
    data1=cart.objects.filter(usercart=user_id,status=0)
    a=cart.objects.filter(usercart=user_id,status=0).aggregate(Sum('total'))
    return render(request,"addcart.html",{'data':data1,'a':a})

def remove(request,id):
    cart.objects.filter(id=id).delete()
    return redirect('addtocart')

def card(request):
    data=category.objects.all()
    return render(request,"card.html",{'data':data})

def card1(request,cat):
    if(cat == "all"):
     data1=product.objects.all()
    else:
     data1=product.objects.filter(categories=cat)
    return render(request,"card1.html",{'data1':data1})

def feedbackdata(request):
    return render(request,"feedback.html")

def feedbackinfo(request):
    if request.method =='POST':
        email=request.POST['email']
        feedbacks=request.POST['feedbacks']
        data=feedback(email=email,feedbacks=feedbacks)
        data.save()
    return redirect('user')

def logininfo(request):
    return render(request,"login.html")

def registers(request):
    return render(request,"register.html")

def registerinfo(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        mail=request.POST['mail']
        contact1=request.POST['contact1']
        data=register(username=username,password=password,mail=mail,contact1=contact1)
        data.save()
    return redirect('user')


def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if register.objects.filter(username=username,password=password).exists():
           data = register.objects.filter(username=username,password=password).values('id','contact1','mail').first()
           request.session['u_id'] = data['id']
           request.session['contact1_u'] = data['contact1'] 
           request.session['mail_u'] = data['mail'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('user') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('user')

def userlogout(request):
    del request.session['u_id']
    del request.session['contact1_u']
    del request.session['mail_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('logininfo')


def view(request,id):
    data1=product.objects.filter(id=id)
    return render(request,"viewcard1.html",{'data1':data1})

