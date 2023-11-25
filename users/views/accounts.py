from django.views import View
from django.shortcuts import render,redirect
from users.models import User
from django.contrib.auth import authenticate, login, logout
import random
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib import messages


class LoginFunc(View):
	
	''' here we are presenting a docstring that represents login function'''

	## templates using for this function
	templates_name = 'users/login.html'
	## ends here templates using for this function

	def get(self,request):
		context = {}
		try:
			context['sucess_msg'] = self.request.GET.get('sucess_msg')
			return render(request,self.templates_name,context)
		except Exception as e:
			print(e)
			return render(request,self.templates_name,context)

	def post(self,request):
		context = {}
		try:
			email = request.POST.get("email").strip().lower()
			if not email:
				context['msg'] = 'Error ! Please, Enter Your email'
				return render(request,self.templates_name,context)

			password = request.POST.get("password").strip()
			if not password:
				context['msg'] = "Error ! Please, Enter Your password"
				return render(request,self.templates_name,context)

			email_check = User.objects.filter(email = email)
			if email_check:
				print("\n" * 3)
				print(email_check)
				print("\n" * 3)
				if email_check[0].is_active == True :
					username_auth = authenticate(username = email_check[0], password = password)
					print("username_auth", username_auth)
					if username_auth:
						login(request,username_auth)
						# context['sucess_msg'] = "Success ! Login Done"
						# return render(request,self.templates_name,context)

						return redirect("/users/product_list/")

					else:
						context['msg'] = 'Error ! Incorrect Username and Password, Please try again'
						return render(request,self.templates_name,context)
				else:
					context['msg'] = 'Error ! Incorrect Username and Password, Please try again'
					return render(request,self.templates_name,context)
			else:
				context['msg'] ='Error ! Incorrect Username, Please try again'
				return render(request,self.templates_name,context)


		except Exception as e:
			print("\n" * 3)
			print(e)
			print("\n" * 3)
			context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
			return render(request,self.templates_name,context)


class LogoutView(View):

	def get(self,request):

		logout(request)
		return redirect('/users/login/?sucess_msg=Success ! Your Account has been Successfully Logout')
