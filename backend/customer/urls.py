from django.urls import path
from customer import views


app_name = "customer"

urlpatterns = [
    path('register/',views.RegisterApi.as_view()),
    path('verify/', views.VerifyOTP.as_view()),
    path("sign-up/", views.register_view, name="sign-up"),
    path("sign-in/", views.login_view, name="sign-in"),
    path("sign-out/", views.logout_view, name="sign-out"),
]
