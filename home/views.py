from django.shortcuts import render_to_response,render
from home.models import case,product,homeInner
# Create your views here.

def index(request):
    caselist=case.objects.all()
    productlist=product.objects.all()
    homeInnerlist=homeInner.objects.all()
    return render(request,'index.html',context={'caselist':caselist,
                  'productlist':productlist,
                  'homeInnerlist':homeInnerlist})





