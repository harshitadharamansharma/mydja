from django.http import HttpResponse
from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product  #. period means current foldr

# Create your views here.
#view funvtion
def index(request):
    product = Product.objects.all()
    # Product.objects.filter()  #filtering product
    # Product.objects.get()   #getting a single method
    # Product.objects.save()   # inserint new or updating single one
    
    return render(request, 'index.html',
                    {'products': product}) 
                    # 3rd argument # a dictioonary that contains the data to be passed to the object
                    #
   
   
    # return render(request, 'index.html')
   # return HttpResponse('Hello KabadEE')
# this returns plain text to the browser or to the client
    # URL mapping:- unifrom resource locator (Address)
    # /product -> index


def new(request):
    return HttpResponse('New productssss')

#def new(request):

# whren a browser sends the https request to server
# when a user navigates to /productss page 
# browser sends ghat http request to django application 
# and hands it on to the index function where the hello kabaad|E is writen

# now we want to display product lkist from the datqqbase at the place of hello kabaadE
