from django.shortcuts import render,redirect
from django.contrib import messages
from Users.models import Users
from django.contrib.auth import login,logout,authenticate
from .forms import *
from random import choices
from string import ascii_letters


def register_page(request,type):
    if type not in ['derakhti','taksathi']:
        return redirect('Account:login_page')

    if request.method == "POST":
        form = AccountRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            user = Users.objects.filter(username=form.cleaned_data['username']).first()
            user.set_password(request.POST['password'])
            user.role = type
            user.save()
            def create():
                identifierـcode = "$" + "".join([choices(list(ascii_letters))[0] for _ in range(10)])
                user_check = Users.objects.filter(identifierـcode=identifierـcode).first()
                if user_check is not None:
                    create()
                else:
                    return identifierـcode
            user.identifierـcode = create()
            user.save()
            login(request,user)

            if user.role == 'taksathi':
                return redirect('Taksathi:taksathi_panel_page')

            elif user.role == 'derakhti':
                return redirect('Derakhti:derakhti_page')



            else:
                return redirect('/')

        else:
            context = {
                'form': form,
            }
            messages.error(request, form.errors)
            return render(request, 'Account/register_page/register_page.html',context)
    return render(request,'Account/register_page/register_page.html')




def login_page(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if user is not None:
                login(request,user)
                if user.role == 'taksathi':
                    return redirect('Taksathi:taksathi_panel_page')

                elif user.role == 'derakhti':
                    return redirect('Derakhti:derakhti_page')

                elif user.role == 'taksathiAdmin':
                    return redirect('Taksathi:taksathi_admin_panel_page')
            else:
                messages.error(request, 'اطلاعات اشتباه است')
                return render(request, 'Account/login_page/login_page.html')

        return render(request,'Account/login_page/login_page.html')
    else:
        return redirect('/')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('Account:login_page')
    else:
        return redirect('Account:login_page')
