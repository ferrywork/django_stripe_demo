# Generated by Django 3.1.12 on 2021-08-17 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_stripeproduct_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripeproductprices',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
