from django.shortcuts import render
from .models import coder,sales,tech,homeInner

# Create your views here.
def team(request):
    homeInnerlist=homeInner.objects.all()
    coderlist=coder.objects.all()
    saleslist=sales.objects.all()
    techlist=tech.objects.all()
    return render(request,'left-sidebar.html',context={'coderlist':coderlist,
                  'saleslist':saleslist,
                  'techlist':techlist,
                  'homeInnerlist':homeInnerlist})