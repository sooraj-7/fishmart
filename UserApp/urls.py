from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('user',views.user,name="user"),
    path('about',views.about,name="about"),
    path('card',views.card,name="card"),
    path('card1/<str:cat>',views.card1,name="card1"),
    path('feedbackinfo',views.feedbackinfo,name="feedbackinfo"),
    path('logininfo',views.logininfo,name="logininfo"),
    path('registers',views.registers,name="registers"),
    path('registerinfo',views.registerinfo,name="registerinfo"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('publicdata',views.publicdata,name="publicdata"),
    path('feedbackdata',views.feedbackdata,name="feedbackdata"),
    path('view/<int:id>',views.view,name='view'),
    path('addcart/<int:id>',views.addcart,name="addcart"),
    path('checkouts',views.checkouts,name="checkouts"),
    path('addtocart',views.addtocart,name="addtocart"),
    path('remove/<int:id>',views.remove,name="remove"),
    path('checkoutdata',views.checkoutdata,name="checkoutdata"),
    path('success',views.success,name="success"),

]