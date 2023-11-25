# Generated by Django 3.1.12 on 2021-08-02 07:55

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import users.models.user
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=75, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{1,50}')], verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{1,50}')], verbose_name='last_name')),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$')])),
                ('trial_expires_on', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paypal_email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('device_token', models.CharField(blank=True, max_length=200, null=True)),
                ('one_time_token', models.CharField(blank=True, max_length=200, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=users.models.user.user_logo_directory_path)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=6, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]