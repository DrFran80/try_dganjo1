from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
from .models import Product

def render_initial_data(request):
    obj = Product.objects.get(id=4)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    my_context ={
        'form' : form
    }
    return render(request, "products/product_create.html",  my_context)
    
def product_create_view(request):
    form = ProductForm(request.POST or None) ## render a form is POST is tre else render empty form
    if form.is_valid():
        form.save()
        form = ProductForm()
    my_context ={
        'form' : form
    }
    return render(request, "products/product_create.html",  my_context)

def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance = obj) ## render a form is POST is true else render empty form
    if form.is_valid():
        print("Saving")
        form.save()
        return redirect('..')

    my_context ={
        'form' : form
    }
    return render(request, "products/product_create.html",  my_context)

def product_detail_view(request, my_id):
    #obj = Product.objects.get(id = my_id)  || 1) No sabe que hacer si el obj no existe
    
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404  || 2) maneja el error DoesNot Exist

    obj = get_object_or_404(Product, id=my_id)
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html",  context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../create/')
    my_context ={
        'object' : obj
    }
    return render(request, "products/product_delete.html",  my_context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
            'object_list':queryset,
    }
    return render(request, 'products/product_list.html', context)