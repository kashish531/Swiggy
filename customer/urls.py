from django.urls import path,include
from .views import *
from customer.views import *

urlpatterns = [
path('login-customer',LoginCustomerViews.as_view())
]