from django.views.generic import View
from django.shortcuts import render,redirect
from users.models import User
from django.contrib.auth import authenticate, login, logout
import random
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib import messages
from users.models import StripeProduct
from django.http import JsonResponse
import stripe,json
from decouple import config

stripe.api_key = config('STRIPE_SECRET_KEY', default='')

class ProductList(View):
	
	''' here we are presenting a docstring that represents it will hit while product listing page'''

	## templates using for this function
	templates_name = 'product/list.html'
	## ends here templates using for this function

	def get(self,request):
		context = {}
		try:
			all_products = StripeProduct.objects.all().order_by('-created_on')
			context['all_products'] = all_products
			return render(request,self.templates_name,context)
		except Exception as e:
			print(e)
			return render(request,self.templates_name,context)


class ProductAdd(View):
	
	''' here we are presenting a docstring that represents it will hit while product add page'''

	## templates using for this function
	templates_name = 'product/add.html'
	## ends here templates using for this function

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

			## getting product_type_name value and validate it 
			product_type_name = self.request.POST.get('product_type_name').strip()
			if not product_type_name:
				context['msg'] = 'Error ! Please Enter Product Name'
				return render(request,self.templates_name,context)
			## ends here getting product_type_name value and validate it 
			check_product_name = StripeProduct.objects.filter(type_name_english = product_type_name)
			if check_product_name:
				context['msg'] = 'Error ! Product Name is already in Use'
				return render(request,self.templates_name,context)



			user_id = request.user.id
			user_instance = User.objects.get(id = user_id)
			product = stripe.Product.create(
			  name=product_type_name,
			)
			type_code = product.get('id')

			check_product_code = StripeProduct.objects.filter(type_code = type_code)
			if check_product_code:
				context['msg'] = 'Error ! Product Code is already in Use'
				return render(request,self.templates_name,context)


			product = stripe.util.convert_to_dict(product)



			StripeProduct.objects.create(type_name_english = product_type_name,stripe_product_json = json.dumps(product), product_id = product.get('id'),type_description_english = product.get('statement_descriptor'), type_code = type_code )
			context['success_msg'] = 'Success ! Product has been successfully save into our database'

			return render(request,self.templates_name,context)

		except Exception as e:
			print(e)
			context['msg'] = 'Error ! Something went wrong please try again later or contact us'
			return render(request,self.templates_name,context)


class ProductEdit(View):
	
	''' here we are presenting a docstring that represents it will hit while product edit page'''

	## templates using for this function
	templates_name = 'product/edit.html'
	## ends here templates using for this function

	def get(self,request):
		context = {}
		try:
			return render(request,self.templates_name,context)
		except Exception as e:
			print(e)
			return render(request,self.templates_name,context)



class DeactivateProducts(View):

	def get(self,request):
		context = {}
		try:
			getting_id = request.GET.get("id")
			getting_obj = StripeProduct.objects.get(id = getting_id)
			if getting_obj.is_active == True:
				getting_obj.is_active = False
				getting_obj.save()
			elif getting_obj.is_active == False:
				getting_obj.is_active = True
				getting_obj.save()

			context['status'] = 200
			return JsonResponse(context)

		except Exception as e:
			print(e)
			context['status'] = 500
			return JsonResponse(context)
