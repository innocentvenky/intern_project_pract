from django.shortcuts import render,redirect
from userapp.models import Register
# Create your views here.
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = Register.objects.get(
            email=email,
            password=password
        )
        if user:
            return redirect('/home/')
        else:
            return render(request,'login.html',{'error':'Invalid email or password'})
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')
    