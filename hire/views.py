from django.shortcuts import render
from hire.models import hire,homeInner

# Create your views here.
def hires(request):
    hirelist=hire.objects.all()
    homeInnerlist=homeInner.objects.all()
    return render(request,'elements.html',context={'hirelist':hirelist,
                  'homeInnerlist':homeInnerlist})