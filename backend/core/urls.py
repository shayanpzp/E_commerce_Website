from django.urls import path
from . import views


urlpatterns = [
    path('sellers/',views.SellerList.as_view()),
]
