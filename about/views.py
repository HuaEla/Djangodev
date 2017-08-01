from django.shortcuts import render
from . import models
from .forms import messageForm


# Create your views here.
def messageview(request):
    homeinner=models.homeInner.objects.all()
    form = messageForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            message=form.save()
            models.message=message
            form = messageForm()
            return render(request, 'contact.html', context={'homeinner':homeinner, 'form': form})
        else:
            form = messageForm()
    return render(request,'contact.html',context={'homeinner':homeinner,'form':form})