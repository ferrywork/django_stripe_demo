from django.views.generic import View
from django.shortcuts import render,redirect
from users.models import User
from django.contrib.auth import authenticate, login, logout
import random
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib import messages
from users.models import StripeProductPrices,StripeProduct
from django.http import JsonResponse
import stripe
from decouple import config

stripe.api_key = config('STRIPE_SECRET_KEY', default='')


class PriceList(View):
	
	''' here we are presenting a docstring that represents it will hit while price listing page'''

	## templates using for this function
	templates_name = 'price/list.html'
	## ends here templates using for this function

	def get(self,request):
		context = {}
		try:
			all_prices = StripeProductPrices.objects.all().order_by('-created_on')
			context['all_prices'] = all_prices
			return render(request,self.templates_name,context)
		except Exception as e:
			print(e)
			return render(request,self.templates_name,context)



class PriceAdd(View):
	
	''' here we are presenting a docstring that represents it will hit while price add page'''

	## templates using for this function
	templates_name = 'price/add.html'
	## ends here templates using for this function

	def get(self,request):
		context = {}
		try:
			all_products = StripeProduct.objects.filter(is_active = True).order_by('-created_on')
			context['all_products'] = all_products
			return render(request,self.templates_name,context)
		except Exception as e:
			print(e)
			return render(request,self.templates_name,context)


	def post(self,request):
		context = {}
		try:
			all_products = StripeProduct.objects.filter(is_active = True).order_by('-created_on')
			context['all_products'] = all_products


			## getting product_id value and validate it 
			product_id = self.request.POST.get('product_id').strip()
			if not product_id:
				context['msg'] = 'Error ! Please Enter Product Id'
				return render(request,self.templates_name,context)
			## ends here getting product_id value and validate it 

			## getting price value and validate it 
			price = self.request.POST.get('price').strip()
			if not price:
				context['msg'] = 'Error ! Please Enter Price'
				return render(request,self.templates_name,context)
			## ends here getting price value and validate it 


			check_product_prices = StripeProductPrices.objects.filter(stripe_product_id__product_id = product_id)
			if check_product_prices:
				context['msg'] = 'Error ! Product have already One Price'
				return render(request,self.templates_name,context)


			price = stripe.Price.create(product=product_id,unit_amount=price,currency='usd',  recurring={'interval': 'month'})

			price_product = stripe.util.convert_to_dict(price)

			print("\n" * 3)
			print("product price", price_product)
			print("\n" * 3)

			product_instance = StripeProduct.objects.get(product_id = product_id,is_active = True)

			StripeProductPrices.objects.create(stripe_product_id = product_instance,price_per_month = price_product.get('unit_amount'), stripe_price_id = price_product.get('id'),stripe_price_json = price_product, country = price_product.get('currency') )
			context['success_msg'] = 'Success ! Product Price has been successfully save into our database'

			return render(request,self.templates_name,context)

		except Exception as e:
			print(e)
			context['msg'] = 'Error ! Something went wrong please try again later or contact us'
			return render(request,self.templates_name,context)


class PriceEdit(View):
	
	''' here we are presenting a docstring that represents it will hit while price edit page'''

	## templates using for this function
	templates_name = 'price/edit.html'
	## ends here templates using for this function

	def get(self,request):
		context = {}
		try:
			return render(request,self.templates_name,context)
		except Exception as e:
			print(e)
			return render(request,self.templates_name,context)



class DeactivatePrice(View):

	def get(self,request):
		context = {}
		try:
			getting_id = request.GET.get("id")
			getting_obj = StripeProductPrices.objects.get(id = getting_id)
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


