from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
]

from django.http import HttpResponse

urlpatterns += [
    path('favicon.ico', lambda request: HttpResponse(status=204)),  # 204 = No Content
]