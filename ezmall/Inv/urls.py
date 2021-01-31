from django.urls import path,re_path

from .import views

urlpatterns = [
    path('',views.dashboard,name='home'),
    re_path('product/',views.product,name='Product'),
    re_path('customer/',views.customer,name='Customer')
]
