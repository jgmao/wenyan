# Create your views here.
from django.shortcuts import render
from ArticalManager.forms import ArticalForm
def showArtical(request):
    if request.method =='POST':
        print "posting"
        form = ArticalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArticalForm()
    return render(request,'artical.html',{'form':form,})            