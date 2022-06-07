from django.shortcuts import render,HttpResponse,render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import registerform

# Create your views here

def index(request):
 return render(request,'index.html')

def signin(request):
  if request.method == 'POST':
   username = request.POST['username']
   password = request.POST['password']
   user = authenticate(username=username,password=password)
   if user is not None:
    login(request,user)
    return redirect('/dashb')
   else:
    return redirect('/login')
  return render(request,'signin.html')


def signup(request):
 if request.method == 'POST':
  un = request.POST['username']
  fn = request.POST['first_name']
  ln = request.POST['last_name']
  em = request.POST['email']
  key = request.POST['password']
  newuser = User.objects.create_user(
     username = un,
     first_name = fn,
     last_name = ln,
     password = key,
     email = em
    )
  newuser.save()
  return HttpResponse('Registerd')

 rf = registerform()
 return render(request,'signup.html',{'f':rf})


@login_required
def dashboard(request):
 return render(request,'dash.html')

@login_required
def signout(request):
 logout(request)
 return redirect('/login')
