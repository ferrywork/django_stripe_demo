from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from users.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import pdb
from users.register_serializer import RegisterSerializer

class Register(View):

    templates_name = 'users/register.html'

    def get(self,request):
        context = {}
        try:
            return render(request,self.templates_name,context)
        except Exception as e:
            print(e)
            return render(request,self.templates_name,context)

    def post(self,request):
        context = {}
        try:
            pdb.set_trace()
            reqdata = request.POST

            form =RegisterSerializer(data=reqdata)
            if not form.is_valid():
                context['msg'] = form.errors
                return render(request,self.templates_name,context)

            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            phone_number = request.POST.get("phone_number")
            email = request.POST.get("email").strip().lower()
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")

            #check password
            if(password != confirm_password):
                context['msg'] = '"Passwords did not match!"'
                return render(request,self.templates_name,context)
            elif len(password) < 5:
                context['msg'] = '"Password length must be atleast 6 characters!"'
                return render(request,self.templates_name,context)

            # check existing email
            if User.objects.filter(email=email):
                context['msg'] = '"Account already exists!"'
                return render(request,self.templates_name,context)

            # create user
            user = User(first_name=first_name,last_name=last_name, phone = phone_number, email=email, username = email)
            user.set_password(password)
            user.save()
            
            # send mail
            try:                
                subject, from_email, to = "Verify your Email Address", settings.EMAIL_HOST_USER, [user.email]
                name =user.first_name+' '+ user.last_name
                message="Hello " + name + ",\nYou have successfully registered for Stripe Django, please go to login page and login into your account.\n\nThanks,\nStripe Django Team"
                send_mail(subject,message,from_email,to, fail_silently=False)
            
            except Exception as E:
                print(E)
                context['msg'] = '"Error sending Mail"'
                return render(request,self.templates_name,context)

            return redirect('/users/login/')

        except Exception as e:
            context['msg'] = '"Something went wrong!, trace:"'  + str(e)
            return render(request,self.templates_name,context)
