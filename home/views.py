from django.shortcuts import render
from home.models import dataMahasiswa
from home.forms import FormMahasiwa
# Create your views here.
def home(request):
    data = dataMahasiswa.objects.all()
    context = {
        'data': data,
    }
    return render(request,'home.html', context)

def formulir(request):
    form = FormMahasiwa()
    
    context = {
        'form': form,
    }
    return render(request,'tambah.html',context)