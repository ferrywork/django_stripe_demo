from rest_framework.views import APIView
import random
from users.models import User
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login
from knox.models import AuthToken
from django.template.loader import render_to_string




class LoginScreen(APIView):

	def post(self, request):
		try:
			context = {}
			email = self.request.POST.get('email').strip()
			if not email:
				context['message'] = 'Please Fill out Your Email'
				context['status'] = 100
				return JsonResponse(context)

			password = self.request.POST.get('password')
			email_exist = User.objects.filter(email = email).count()
			if email_exist > 0:
				user_obj = User.objects.get(email = email)
				if user_obj.is_active == 1:
					if user_obj.is_confirm == 1:
						user = authenticate(username = user_obj, password = password)
						if user is not None:
							token = AuthToken.objects.create(user_obj)[1]

							context['status'] = 200
							context['token'] = token
							context['user_id'] = user_obj.id
							context['user_email'] = user_obj.email
							context['phone'] = user_obj.username
							context['message'] = "Login Successfully"

							return JsonResponse(context)
						else:
							context = {"status":100,"message":"Incorrect email or password, please try again"}
							return JsonResponse(context)
					else :
						context = {"status":100,"message":"Sorry ! Your account is not confirmed yet"}
						return JsonResponse(context)
				else:
					context = {"status":100,"message":"Sorry, Your account is temporarily disabled,Please contact our support team"}
					return JsonResponse(context)
			else:
				context = {"status":100,"message":"Incorrect Username or password, please try again"}
				return JsonResponse(context)
		except Exception as e:
			print("\n" * 3)
			print("Exception at Login is",e)
			print("\n" * 3)
			context = {"status":500,"message":"Something Going Wrong ! Please try again later or contact us"}
			return JsonResponse(context)
