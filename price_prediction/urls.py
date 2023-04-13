from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('predict-price',views.predict),
    path('login/',views.login),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path('buy/',views.buy),
    path('sell/',views.sell),
    path('car-details/',views.car_details),
]