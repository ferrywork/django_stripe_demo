# Generated by Django 3.1.12 on 2021-08-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210817_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripeproduct',
            name='type_description_english',
            field=models.TextField(blank=True, null=True),
        ),
    ]
