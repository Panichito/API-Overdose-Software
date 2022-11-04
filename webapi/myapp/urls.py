from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('api/newuser', register_newuser),
    path('api/authenticate', authentiate_app),
    path('api/all-medicine', all_medicine),
    path('api/post-record', post_record),
]