from django.shortcuts import render
from .models import News,Category

# Create your views here.


def index(request):
    news = News.objects.all()
    return render(request,"index.html",{'data':news})

def category(request):
    return render(request,"category.html")

def contact(request):
    return render(request,"contact.html")

def single(request,id):
    news2 = News.objects.get(id=id)
    return render(request,"single.html",{'data':news2})

def base(request,name):
    category = Category.objects.get(name=name)
    return render(request,"base.html",{'category':category})

# def Search(request):
#     if 'q' in request:
#         q = request.GET('q')
#         news = News.objects.filter(description__icontain=q)
#     else:
#         news = News.objects.all()
#         q = None

#     return render(request,'index.html',{"news":news,'q':q})

