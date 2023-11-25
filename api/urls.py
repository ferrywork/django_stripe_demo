from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import UserSignUp,LoginView
from api.login import LoginScreen
urlpatterns = [
    path('register/', UserSignUp.as_view(),name="register"),
    path('login/', LoginScreen.as_view()),
    # path('profile/', MyProfile),
    # path('avatar/', Avatar),
    # path('change-password/', ChangePassword),
    # path('forgot-password/', ForgotPassword),
    # path('logout/', Logout),
    # path('home/', Dashboard),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
