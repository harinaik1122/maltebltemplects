from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hari_str(request):
    return HttpResponse('<h1>thi is hari</h1>')

def harihtml(request):
    return render(request,'harihtml.html')
