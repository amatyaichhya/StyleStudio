from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tops', views.listing, name='listing'),
    path('tops/product_detail', views.detail, name='detail')
]