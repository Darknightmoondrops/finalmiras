from django.shortcuts import render,redirect,HttpResponse
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from random import choices
from string import ascii_lowercase,ascii_letters
from django.shortcuts import get_object_or_404
from extensions.derakhti.amount_purchased import amount_purchased
from .models import *
from .serializers import *
from .models import *


def derakhti_page(request):
    if request.user.is_authenticated:
        user = Users.objects.filter(id=request.user.id).first()
        if user.role == 'derakhti':
            return render(request,'derakhti/derakhti_page/derakhti_page.html')
        else:
            return redirect('Account:login_page')
    else:
        return redirect('Account:login_page')



def pardakht_page(request):
    if request.user.is_authenticated:
        cart = DerakhtiProductsCarts.objects.filter(user_id=request.user.id)
        products = DerakhtiProductsOrders.objects.filter(cart_id=cart.id,payment_status=False).all()

        for p in products:
            p.payment_status = True
            p.price_drsd = p.price
            p.price = p.price - ((p.price*10)//100)
            p.save()

        return HttpResponse('Ok')

    else:
        return redirect('Account:login_page')




