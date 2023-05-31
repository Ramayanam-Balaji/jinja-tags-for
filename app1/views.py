from django.shortcuts import render

# Create your views here.
def prabhas(request):
    d={'name':'prabhas'}
    return render(request,'prabhas.html',d)
