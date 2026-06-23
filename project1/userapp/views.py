
from django.shortcuts import render,redirect
from userapp.models import Register
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        date_of_birth=request.POST.get('date_of_birth')
        phone_number=request.POST.get('phone_number')
        state=request.POST.get('state')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        pincode=request.POST.get('pincode')
        Register.objects.create(first_name=first_name, last_name=last_name,email=email,password=password,date_of_birth=date_of_birth,phone_number=phone_number,state=state,city=city,gender=gender,pincode=pincode)
    return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try :
            user = Register.objects.get(
                email=email,
                password=password
            )
            return redirect('success/')
        except Register.DoesNotExist:
            return redirect('login/',{'error':'Invalid email or password'})
    return render(request,'login.html')
        
def success(request):
    return render(request,'success.html')
        
    

