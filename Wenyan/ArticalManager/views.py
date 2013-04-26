# Create your views here.
from django.shortcuts import render
from ArticalManager.forms import ArticalForm
def showArtical(request):
    if request.method =='POST':
        form = ArticalForm(request.POST)
    else:
        form = ArticalForm()
    return render(request,'artical.html',{'form':form,})            