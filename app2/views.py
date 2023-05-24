from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def naik(request):
    return HttpResponse('<h1><center>hello warld</h1></center>')

def naik1(request):
    return render(request,'naik1.html')
