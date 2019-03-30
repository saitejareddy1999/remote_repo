from django.shortcuts import render

# Create your views here.
def connect4view(request):
    return render(request,'firstapp/connect4.html')
