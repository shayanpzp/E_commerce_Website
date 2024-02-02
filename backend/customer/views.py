from django.shortcuts import redirect, render
from .forms import UserRegisterForm, ChangePasswordForm , PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from customer.models import User
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .emails import send_otp_via_email
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views import View




# User = settings.AUTH_USER_MODEL

 
class RegisterApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print("11111111")
                send_otp_via_email(serializer.data['email'])
                print("22222222")
                return Response({
                    'status' : 200,
                    'message' : 'success & check email',
                    'data' : serializer.data,
                })
            return Response({
                    'status' : 400,
                    'message' : 'something is wrong !',
                    'data' : serializer.errors
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
    
    
    
class RegisterView(FormView):
    template_name = "customer/sign-up.html"
    form_class = UserRegisterForm

    def form_valid(self, form):
        new_user = form.save()
        username = form.cleaned_data.get("username")
        messages.success(self.request, f"Hey {username}, Your account was created successfully.")
        new_user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        return redirect("core:index")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))





class LoginView(View):
    template_name = "customer/sign-in.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request, f"Hey you are already logged in.")
            return redirect("core:index")
        return render(request, self.template_name)

    def post(self, request):
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
        except User.DoesNotExist:
            messages.warning(request, f"User with {email} does not exist.")

        return render(request, self.template_name)




class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You logged out.")
        return redirect("customer:sign-in")
    
    
    


class ChangePasswordView(FormView):
    template_name = "customer/change_password.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy('core:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))