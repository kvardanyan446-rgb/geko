from django.urls import path
from .views import product_details, product_list
 
urlpatterns = [
    path('', product_list),
    path('<int:product_id>/')
]