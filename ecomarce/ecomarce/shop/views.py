from django.shortcuts import render
from django.http import HttpResponse
from . models import Product,Contact
from math import ceil
# Create your views here.
def product(request):
    allprods=[]
    catprods=Product.objects.values("category")
    cats={item["category"] for item in catprods}
    for cat in cats:
        prods=Product.objects.filter(category=cat)
        n=len(prods)
        nSlides=n//4 + ceil(n/4)- (n//4)
        allprods.append([prods,range(1,nSlides),nSlides])

    params={'allProds':allprods}    
    return render(request,'shop/products.html',params)

def shop(request):
    return render(request, 'shop/index.html')
        
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        msg = request.POST.get('msg', '')
        contact = Contact(name=name, email=email,msg=msg)
        contact.save()
        
        

    return render(request, 'shop/contact.html')
        
def productview(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    
    return render(request, 'shop/productview.html', {'product':product[0]})
        
def search(request):
    return render(request, 'shop/search.html')
def about(request):
    return render(request, 'shop/about.html')
        
def checkout(request):
    return render(request, 'shop/checkout.html')
        
def traking(request):
    return render(request, 'shop/traking.html')
# def index(request):
#     objects = Product.objects.all()
#     context = {
#             'objects' : objects
#             }
#     return render(request,'shop/index.html',context)
    