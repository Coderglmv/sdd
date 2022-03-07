from django.shortcuts import render, redirect
from django.views import View
from .models import (MainPage, MainAboutProduct,
 Connection, About_us, Mini_aboutUs, Products)
from .forms import ConnectForm
# Create your views here.



def main(request):
    mainpage = MainPage.objects.all()
    aboutProduct = MainAboutProduct.objects.all()
    if request.POST:
    	name = request.POST['name']
    	email = request.POST['email']
    	phone = request.POST['phone']
    	requestt = request.POST['requestt']
    	Connection(name=name,phone=phone,email=email,special_request=requestt).save()
    	return redirect('cofe:main')
    
    return render(request, 'block_main.html', {'main':mainpage, 'aboutProduct': aboutProduct})


def about_us(request):
    about_us = About_us.objects.all()
    miniAboutus = Mini_aboutUs.objects.all()
    return render(request, 'about_us.html',{
        'about_us': about_us,
        'mini': miniAboutus
        })


def shopView(request):
    products = Products.objects.all()
    return render(request, 'shop.html',{'products':products})

def bookView(request, pk):
    product = Products.objects.get(id=pk)
    return render(request, 'book.html',{'product':product})    

def database(request):
	mainPage = MainPage.objects.all()
	aboutProduct = MainAboutProduct.objects.all()
	connection = Connection.objects.all()
	return render(request, 'database.html',{
		'main':mainPage,
		'aboutProduct': aboutProduct,
		'connection':connection
		})     