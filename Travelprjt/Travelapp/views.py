from django.shortcuts import render
from .models import place,photo


# Create your views here
def demo(request):
    obj=place.objects.all()
    obj1 = photo.objects.all()
    return render(request,"index.html",{'result':obj,'result1': obj1})




