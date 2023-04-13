# Create your views here.

import pickle
import numpy as np
from django.shortcuts import render,redirect
from .models import Car
from .forms import CarForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth,User


# join base dir
BASE_DIR = ""

# model = pickle.load(open('C:\\Users\\Hashim\\Desktop\\car-trade\\car_trade\\price_prediction\\random_forest_regression_model.pkl', 'rb'))
model = pickle.load(open('C:\\Users\\91963\\Desktop\\car-price-main\\car_trade\\price_prediction\\random_forest_regression_model.pkl', 'rb'))
def index(request):
    return render(request, 'home.html')

@login_required(login_url="/login")

def predict(request):
    # form = CarForm()
    if request.method == 'POST':
        year = int(request.POST['year'])
        year=2023-year
        present_price = int(request.POST['present_price'])
        kms_driven = int(request.POST['kms_driven'])
        kms_driven2 = np.log(kms_driven)
        owner = int(request.POST['owner'])
        fuel_type_petrol = request.POST['fuel_type_petrol']
        fuel_type_diesel = not fuel_type_petrol
        seller_type_individual = request.POST['seller_type_individual']
        transmission_manual = request.POST['transmission_mannual']
        if(fuel_type_petrol=='Petrol'):
                fuel_type_petrol=1
                fuel_type_diesel=0
        else:
            fuel_type_petrol=0
            fuel_type_diesel=1
        if(seller_type_individual=='Individual'):
            seller_type_individual=1
        else:
            seller_type_individual=0	
        if(transmission_manual=='Mannual'):
            transmission_manual=1
        else:
            transmission_manual=0

        prediction = model.predict([[present_price, kms_driven2, owner, year, fuel_type_diesel, fuel_type_petrol,seller_type_individual, transmission_manual]])
        # prediction = model.predict([[present_price, kms_driven, owner, 2020 - year, fuel_type_diesel, fuel_type_petrol,
        #                              seller_type_individual, transmission_manual]])
        output = round(prediction[0], 2)
        return render(request, 'predict.html', {'output': output})

    return render(request, 'predict.html')

def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method=='POST':
        username=request.POST['username']
        passwd=request.POST['passwd']
        user=auth.authenticate(username=username,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:return HttpResponse("Invalid email or password")
        return HttpResponse("{} {}".format(email,passwd))
    return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("/")
    return render(request, 'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        passwd=request.POST['passwd']
        user=User.objects.create_user(username=username,email=email,password=passwd)
        auth.login(request,user)
        return redirect("/")
    return render(request, 'signup.html')

def buy(request):
    if request.user.is_authenticated:
        return render(request,"buy.html")
    return redirect('/login')


def sell(request):
    if request.user.is_authenticated:
        return render(request,"sell.html")
    return redirect('/login')

def car_details(request):
    if request.user.is_authenticated:
        return render(request,"cardetails.html")
    return redirect('/login')