from django.db import models
import uuid 
import jsonfield
from users.models import User



class UserSubscription(models.Model):

    ''' demonstrate docstring to confirm that this model will store user subscription into our database  '''
    class Meta:
       db_table  = "user_subscription"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    subscription_number = models.CharField(max_length = 200, unique = True)
    stripe_product_id = models.CharField(max_length = 100)
    payment_amount = models.FloatField()
    start_on = models.DateField()
    expires_on = models.DateField()
    stripe_subscription_create_json = jsonfield.JSONField()
    stripe_subscription_cancel_json = jsonfield.JSONField()
    stripe_subscription_modify_json = jsonfield.JSONField()
    susbcription_id = models.CharField(max_length = 200, unique = True)
    subscription_status = models.CharField(max_length = 200)
    date_archived = models.DateField(null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user_instance = models.ForeignKey(User, on_delete = models.CASCADE)

class user_subscription_monthly_payments(models.Model):

    '''demonstrate docstring to confirm that this model will store stripe product prices information in our database  '''

    class Meta:
       db_table  = "user_subscription_monthly_payments"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user_subscription_id = models.ForeignKey(UserSubscription, on_delete = models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.DateField()
    expiry_date = models.DateField()

    is_deleted = models.BooleanField(default = False)
    payment_json = jsonfield.JSONField()
    invoice_id = models.CharField(max_length = 200, null = True, blank = True)

    date_archived = models.DateField(null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class user_monthly_invoice(models.Model):

    '''demonstrate docstring to confirm that this model will store user monthly invoices information into our database  '''

    class Meta:
       db_table  = "user_monthly_invoice"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    invoice_number = models.CharField(max_length = 200, unique = True)
    user_instance = models.ForeignKey(User, on_delete = models.CASCADE)

    invoice_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class UserInvitation(models.Model):

    '''demonstrate docstring to confirm that this model will store user invitation information into our database  '''
    class Meta:
       db_table  = "user_invitation"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(max_length=70,unique= True)
    trial_days = models.IntegerField()
    expiry = models.DateField()
    code = models.CharField(max_length = 100, unique = True)
    is_used = models.BooleanField(default = False)
    accepted_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class ProductUpdates(models.Model):

    '''demonstrate docstring to confirm that this model will store product related information into our database  '''
    class Meta:
       db_table  = "user_product_updates"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    stripe_product_id = models.ForeignKey(UserSubscription,on_delete = models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
