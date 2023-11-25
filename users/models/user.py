from django.db import models
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.core import validators
import re
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager
import uuid 


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    '''demonstrate docstring to confirm this is custom user model that we have inherit from auth user model where we will store user related information into out database'''

    class Meta:
       db_table  = "auth_user"

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    username        = models.CharField(_('username'), max_length=75, unique=True, help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators = [ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid') ])
    first_name      = models.CharField(('first_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50, null=True,blank=True)
    last_name       = models.CharField(('last_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    
    is_staff = models.BooleanField(default=0)
    is_active = models.BooleanField(('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    phone = models.CharField(validators=[RegexValidator( '^[0-9]{10}$')],max_length=12, null=True,blank=True,unique=True)
    trial_expires_on = models.DateTimeField(null = True, blank = True)


    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects         = UserManager()
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name+" "+self.last_name

    def get_short_name(self):
        return self.first_name

        
    def __unicode__(self):
        return self.email

def user_logo_directory_path(instance, filename):
    return '{0}/user_avatar/{1}'.format(get_user_path(instance.user_instance.id), filename)

class UserProfile(models.Model):

    '''demonstrate docstring to confirm that this is user profile model where we will save extra information of the user model '''

    class Meta:
       db_table  = "user_user_profile"

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    paypal_email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    device_token = models.CharField(max_length=200, null = True, blank = True)
    one_time_token = models.CharField(max_length=200, null = True, blank = True)
    avatar = models.ImageField(upload_to = user_logo_directory_path, null = True, blank = True)
    user_instance = models.ForeignKey(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 10, choices = GENDER_CHOICES,null = True, blank = True)
    zipcode = models.CharField(max_length = 6, null = True, blank = True)
    date_of_birth = models.DateField(null = True, blank = True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
