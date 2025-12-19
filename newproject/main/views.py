from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def main_page(request):
    product = [
        {'id':1,'name':'Samsung 24 Ultra','price':1000,'quantity':10,'discount':'5 % '},
        {'id':2,'name':'Iphone 17 pro max','price':2000,'quantity':2,'discount':'10 % '},
        {'id':3,'name':'Xiaoni 17','price':1000,'quantity':100,'discount':'30 % '},

    ]
    if request.method == "POST":
        name = request.POST.get('name')
        return render(request,"index.html",{'products':product,'name':name})
    return render(request,"index.html",{'products':product})

def aboutus(request):
    return render(request, 'aboutus.html')

def get_post(request,id):
    return render(request, 'get_post.html',{'id':id})