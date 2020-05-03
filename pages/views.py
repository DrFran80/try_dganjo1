from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args,**kwargs):
    return render(request, "home.html",{})

def contacts_view(request,*args,**kwargs):
    return render(request, "contacts.html",{})

def about_view(request,*args,**kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": ['a',234, 'hello']
    }
    return render(request, "about.html", my_context)
# Create your views here.
