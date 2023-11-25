from django.http.response import JsonResponse
from users.models.stripe_customer import StripeCustomers
from django.views import View
from django.shortcuts import render,redirect
from users.models import User
import random
from django.contrib import messages
from decouple import config
import stripe
import pdb

class AddCard(View):
	
	''' here we are presenting a docstring that represents add card function'''

	## templates using for this function
	templates_name = 'add_card.html'
	## ends here templates using for this function

	def get(self,request):
		context = {}
		try:
			#pdb.set_trace()
			publisher_key = config('STRIPE_PUBLISHABLE_KEY', default='pk_test_51J7xZ0SI1fVExp8C1ZyN77yFPyMAGIuiLbaqY1y67UqnsMUwyhkikeRphXGI8HVGzl16wSiWbYpsbFDrdCDzrRFJ00fYm6eBIi')
			print("\n" * 3)
			print("publisher_key is ------>", publisher_key)
			print("\n" * 3)

			context['sucess_msg'] = self.request.GET.get('sucess_msg')
			context['publisher_key'] = publisher_key

			logged_in_user_email = request.user.email

			#check if customer exists
			customer_exists = StripeCustomers.objects.filter(email = logged_in_user_email).values('customer_stripe_id')

			if customer_exists:
				context['customer_stripe_id'] = customer_exists[0]['customer_stripe_id']
				print("customer_stripe_id",customer_stripe_id)
			else:
				context['customer_stripe_id'] = ''

			print("context['customer_stripe_id']", context['customer_stripe_id'])

			
			return render(request,self.templates_name,context)
		except Exception as e:
			print(e)
			return render(request,self.templates_name,context)


	def post(self,request):
		try:
			context = {}
			stripe.api_key = config('STRIPE_SECRET_KEY', default='sk_test_51J7xZ0SI1fVExp8Ck8WdF1TQpe6Zp80dFzoVeFtinx0PDe3gcmCzBsH38HgNWGQe0IqyCB22UJNLZliQ1x750CSs00RkgMeZbb')
			print("\n" * 3)
			print("postssssssssssssssssssss")
			print("\n" * 3)

			logged_in_user_email = request.user.email

			# #check if customer exists
			# customer_exists = StripeCustomers.objects.filter(email = logged_in_user_email)

			# if customer_exists:				
			# 	pass

			# else:
			customer_json = stripe.Customer.create(
			name=request.user.first_name+' '+request.user.last_name,
			email = logged_in_user_email,
			)

			customer_id = customer_json.get("id")
			
			StripeCustomers.objects.create(email = logged_in_user_email, 
											customer_stripe_id = customer_id,
											user_instance = User.objects.get(email = logged_in_user_email))
			
			#return render(request,self.templates_name,context)
			data = {'customer_stripe_id':customer_id, 'status':200}
			return JsonResponse(data)
			#return self.render_to_response(data)

		except Exception as e:
			context['msg'] = '"Something went wrong!, trace:"'  + str(e)
			return render(request,self.templates_name,context)
