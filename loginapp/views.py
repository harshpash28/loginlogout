from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def uregister(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        context = {}
        if uname =='' or upass =='' or ucpass =='':
            context['errmsg'] = "fields cannot be empty"
            return render(request,'register.html',context)
        elif upass != ucpass:
            context['errmsg'] = "password cannot match"
            return render(request,'register.html',context)
        else:
            try:
                u = User.objects.create(username = uname)
                u.set_password(upass)
                u.save()
                context = {}
                context['success'] = "user created successfully"
                return render(request,'register.html',context)
            except Exception:
                context['errmsg'] = "user already created"
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')

def ulogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        context = {}
        if uname == '' or upass == '':
            context['errmsg'] = "fields cannot be empty"
            return render(request,'login.html',context)
        else:
            u = authenticate(username = uname, password = upass)
            if u is not None:
                login(request,u)
                return redirect('/index')
            else:
                context['errmsg'] = "invalid user and password"
                return render(request,'login.html',context)
    else:
        return render(request,'login.html')

def ulogout(request):
    logout(request)
    return render(request,'index.html')

