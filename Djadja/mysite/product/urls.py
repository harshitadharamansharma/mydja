from django.urls import path
from . import views # for importing views module from the current folder

# import views --> views is kinda generic name / and with dependencies with other libraries called viewswith that syntax / and this could lead to import some other views module / with same name 

# views.index()

 # URL mapping:- unifrom resource locator (Address)
    # /product -> index

#/products
#/prodects/1/detail
#/products/new
# various url with app function

urlpatterns = [

    path('',views.index), # just passing it, django ewill take  care to calling the function at the run time, when the client send an https request to server, so here we should not call it
    path('new',views.new) 


]