from django.core.paginator import Paginator,EmptyPage,InvalidPage

from django.db.models import Q
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import *

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    obj1=None
    if c_slug != None:
        c_page=get_object_or_404(categ,slug=c_slug)  
        obj1=shop.objects.filter(cate=c_page,available=True)
    else:
        obj1=shop.objects.all().filter(available=True)
        
    cat=categ.objects.all()

#  ---------------------------------------page------------------------------------   

    p=Paginator(obj1,3)   #represent how many items u want to display

    page=int(request.GET.get('page',1))   #fetch page num from url(href-page)
       

    try:
        pro=p.page(page)  #p=paginator, p.page to display the modules in the page
    except(EmptyPage,InvalidPage):  #try,except function is used to prevent the error occuring
        pro=p.page(p.num_pages)

# ------------------------------------end------------------------------------------

    return render(request,'index.html',{'data1':cat,'data2':obj1,'pr':pro})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


def search(request):
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=shop.objects.all().filter(Q(name__icontains=query)|Q(desc__icontains=query),available=True)

    return render(request,'search.html',{'pr':prod})