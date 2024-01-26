from django.shortcuts import redirect, render
from customer.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from customer.models import User
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .email import send_otp_via_email

# User = settings.AUTH_USER_MODEL

 
class RegisterApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status' : 200,
                    'message' : 'success & check email',
                    'data' : serializer.data,
                })
            
            return Response({
                    'status' : 400,
                    'message' : 'something is wrong !',
                    'data' : serializer.errors,
                })
        except Exception as error:
            print(error)
            
            
class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)
            
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                
                
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                    'status' : 400,
                    'message' : 'something is wrong !',
                    'data' : 'Invalid email',
                })
                    
                if user[0].otp != otp:
                    return Response({
                    'status' : 400,
                    'message' : 'something is wrong !',
                    'data' : 'Wrong Otp',
                })
                
                user = user.first()
                user.is_verified = True
                user.save()
                    
                
                
                return Response({
                    'status' : 200,
                    'message' : 'user verified',
                    'data' : {},
                })
            
            
            return Response({
                    'status' : 400,
                    'message' : 'something is wrong !',
                    'data' : serializer.errors,
                })
            
            
        except Exception as error:
            print(error)
    
    
    
def register_view(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, You account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
                                )
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegisterForm()
        
    context = {
        'form' : form,
    }
    
    return render(request, "customer/sign-up.html", context)




def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey you are already logged in.")
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
        
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in.")
                return redirect("core:index")
            else:
                messages.warning(request, f"User with {email} does not exist. Create an account.")
                
        except:
            messages.warning(request, f"User with {email} does not exist.")
            
            
    return render(request, "customer/sign-in.html")




def logout_view(request, ):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("customer:sign-in")
    
    
    