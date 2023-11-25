from django.db import models
import uuid 
import jsonfield
from users.models import User





class StripeCustomers(models.Model):

    '''demonstrate docstring to confirm that this model will store stripe customer information in our database  '''
    class Meta:
       db_table  = "user_stripe_customers"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(max_length=70, unique= True)
    customer_stripe_id = models.CharField(max_length = 200, unique = True)
    user_instance = models.ForeignKey(User, on_delete = models.CASCADE)
    date_archived = models.DateField(null = True, blank = True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class StripeCustomersCards(models.Model):

    '''demonstrate docstring to confirm that this model will store stripe customer cards information in our database  '''
    class Meta:
       db_table  = "user_stripe_customers_cards"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    stripe_customer_instance = models.ForeignKey(StripeCustomers, on_delete = models.CASCADE)
    customer_stripe_id = models.CharField(max_length = 200, unique = True)
    payment_json = jsonfield.JSONField()
    card_name = models.CharField(max_length = 100)
    payment_id = models.CharField(max_length = 100)
    exp_month = models.CharField(max_length = 100)
    exp_year = models.CharField(max_length = 100)
    last_4 = models.CharField(max_length = 100)
    is_deleted = models.BooleanField(default = False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
