from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from validate_email import validate_email
from datetime import datetime
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .models import MemberDetail
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
# from django.contrib.auth.tokens import PasswordResetTokenGenerator as token_check
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
class RegistrationView(View):
    def get(self,request):
        return render(request,'user/register.html')

    # Functoin for storing formvaleues
    def post(self,request):
        context = {
            'data':request.POST,
            'has_error':False
        }
        
        # data recive from form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')


        if not validate_email(email):
            messages.add_message(request,messages.ERROR,'Please Enter Valid Email')
            context['has_error']=True


        if len(password)<6:
            messages.add_message(request,messages.ERROR,'Password Length at least 6 characters')
            context['has_error']=True


        if MemberDetail.objects.filter(user_name=username):
            messages.add_message(request,messages.ERROR,'UserName Already Taken')
            context['has_error']=True

        if MemberDetail.objects.filter(email=email):
            messages.add_message(request,messages.ERROR,'This email Already Taken')
            context['has_error']=True  

        if context['has_error']:
            return render(request,'user/register.html',context)
        
        user = MemberDetail(user_name=username,email=email)
        # user.user_name=username
        user.first_name=first_name
        user.last_name=last_name
        # user.email=email
        user.contact=contact
        user.set_password(password)
        # userta.created_at = datetime.now()
        user.ip_address = '192.168.0.1'
        user.is_active = False
        user.save()


        current_site = get_current_site(request)
        print(current_site)
        email_subject = 'Activate YOur Account'
        message = render_to_string('user/activate.html',
        {
            'user':user,
            'domain':current_site,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        }
        )

        # print(message)

        email_message = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
        email_message.send()



        messages.add_message(request,messages.SUCCESS,'Account Created Sucess')

        return redirect('register')




class ActivationAccountView(View):

    def get(self,request,uidb64,token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = MemberDetail.objects.get(pk=uid)
        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user,token):
            user.is_active = True
            user.save()
            messages.add_message(request,messages.INFO,'Account Activated Sucess')
            return redirect('register')

        return HttpResponse('some thing went wring')


# Create your views here.
def index(request):
    return render(request,'user/index.html')
