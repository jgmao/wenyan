# Create your views here.
from django.shortcuts import render
from ArticalManager.forms import ArticalForm
from ArticalManager.models import Artical
def editArtical(request):
    if request.method =='POST':
        print "posting"
        form = ArticalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArticalForm()
    return render(request,'edit_artical.html',{'form':form,})            

def listArtical(request):
    articals = Artical.objects.all();
    #if not articals
    return render(request,'list_artical.html',{'articals':articals,})   

def showArtical(request, id):
    artical = Artical.objects.get(pk=id)
    return render(request,'show_artical.html',{'artical':artical,})

def goHome(request):
    return render(request,'home.html')