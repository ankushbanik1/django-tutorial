from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop(request):
    return render(request, 'shop/index.html')
    
def about(request):
    return render(request, 'shop/about.html')
        
def contact(request):
    return render(request, 'shop/contact.html')
        
def productview(request):
    return render(request, 'shop/productview.html')
        
def search(request):
    return render(request, 'shop/search.html')
        
def checkout(request):
    return render(request, 'shop/checkout.html')
        
def traking(request):
    return render(request, 'shop/traking.html')

    