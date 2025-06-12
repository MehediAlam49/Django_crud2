from django.shortcuts import render,redirect
from product.models import *

def home(request):
    return render(request, 'home.html')
def addProduct(request):
    if request.method == 'POST':
        product = productModel(
            name = request.POST.get('name'),
            category = request.POST.get('category'),
            price = request.POST.get('price'),
        )
        product.save()
        return redirect('productList')
    return render(request, 'addProduct.html')
def editProduct(request,id):
    productData = productModel.objects.get(id=id)
    if request.method == 'POST':
        product = productModel(
            id = id,
            name = request.POST.get('name'),
            category = request.POST.get('category'),
            price = request.POST.get('price'),
        )
        product.save()
        return redirect('productList')
    return render(request, 'editProduct.html', {'product': productData})
def deleteProduct(request,id):
    product = productModel.objects.get(id=id).delete()
    return redirect('productList')
def productList(request):
    productData = productModel.objects.all()
    return render(request, 'productList.html', {'productData':productData})