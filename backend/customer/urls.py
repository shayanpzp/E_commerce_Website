from django.urls import path
from customer import views


app_name = "customer"

urlpatterns = [
    path('register/',views.RegisterApi.as_view()),
    path('verify/', views.VerifyOTP.as_view()),
    path("sign-up/", views.RegisterView.as_view(), name="sign-up"),
    path("sign-in/", views.LoginView.as_view(), name="sign-in"),
    path("sign-out/", views.LogoutView.as_view(), name="sign-out"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change-password"),
]
