from django.core.mail import send_mail
from django.conf import settings
from .models import User
import random



def send_otp_via_email(email):
    subject = 'Your account verification email.'
    otp = random.randint(1000, 9999)
    message = f'Your otp code is : {otp} '
    email_form = settings.EMAIL_HOST
    send_mail(subject, message, email_form, [email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()