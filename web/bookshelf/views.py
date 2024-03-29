from django.shortcuts import render, redirect, get_object_or_404
from .models import info
from django.contrib.auth.models import auth, User
from django.contrib import messages


# Create your views here.
def index(request):

    dests = info.objects.all()
    contex={
        "object_list":dests
        }
    return render(request,'index.html',contex)

def contacts(request):
    return render(request,'contacts.html')

def team(request):
    return render(request,'team.html')

# Create your views here.

def loginpage(request):
    if request.method == 'POST':

        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request ,username=username ,password = password)
        
        if user is not None:
             auth.login(request, user)
             return redirect('index')
           
        else:
             messages.info(request,'**Invalid Data')
             return redirect('login')

    else:
        return render(request,'login.html')






def register(request):

    if request.method == 'POST':
        
        first_name=request.POST['first_name']  
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('index')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')



    else:
        return render(request,'register.html')



def mt(request,id):
    each_info = get_object_or_404(info ,id = id)
    context={
        'mt':each_info
        }
    return render(request,'mt.html',context)


def logoutpage(request):
    auth.logout(request)
    return redirect('index')