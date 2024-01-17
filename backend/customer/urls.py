from django.urls import path
from customer import views


app_name = "customer"

urlpatterns = [
    path("sign-up/", views.register_view, name="sign-up")
]
