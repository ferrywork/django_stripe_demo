from django.urls import include, path
from .views import *
from users.views.register import Register
urlpatterns = [
    # path('all-harvest/',HarvestAPIView.as_view()),
    # path('all-bread/', BreadAPIView.as_view()),
    path('login/', LoginFunc.as_view(), name = 'LoginFunc'),
    path('logout/', LogoutView.as_view(), name = 'LogoutView'),


    path('product_add/', ProductAdd.as_view(), name = 'ProductAdd'),
    path('product_edit/', ProductEdit.as_view(), name = 'ProductEdit'),
    path('product_list/', ProductList.as_view(), name = 'ProductList'),
    path('deactivate_product/', DeactivateProducts.as_view(), name = 'DeactivateProducts'),


    path('price_list/', PriceList.as_view(), name = 'PriceList'),
    path('PriceAdd/', PriceAdd.as_view(), name = 'PriceAdd'),
    path('PriceEdit/', PriceEdit.as_view(), name = 'PriceEdit'),
    path('DeactivatePrice/', DeactivatePrice.as_view(), name = 'DeactivatePrice'),


    path('register/', Register.as_view(), name = 'Register'),
    path('add_card/', AddCard.as_view(), name = 'AddCard')

    ]