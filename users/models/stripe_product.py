from django.db import models
import uuid 
import jsonfield
from users.models import User



class StripeProduct(models.Model):

    ''' demonstrate docstring to confirm that this model will store stripe product information in our database  '''

    class Meta:
       db_table  = "user_stripe_product"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    stripe_product_json = jsonfield.JSONField()
    type_code = models.CharField(max_length = 200, unique = True)
    type_name_english = models.CharField(max_length = 200, unique = True)
    type_description_english = models.TextField(null = True, blank = True)
    product_id = models.CharField(max_length = 200)
    date_archived = models.DateField(null = True, blank = True)
    is_active = models.BooleanField(default = True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



class StripeProductPrices(models.Model):

    class Meta:
       db_table  = "user_stripe_product_prices"

    '''demonstrate docstring to confirm that this model will store stripe product prices information in our database  '''

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    stripe_product_id = models.ForeignKey(StripeProduct, on_delete = models.CASCADE)
    country = models.CharField(max_length = 200)
    price_per_month = models.FloatField()
    stripe_price_id = models.CharField(max_length = 100, unique = True)
    stripe_price_json = jsonfield.JSONField()

    date_archived = models.DateField(null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default = True)
    updated_on = models.DateTimeField(auto_now=True)
