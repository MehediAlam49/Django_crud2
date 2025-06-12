from django.shortcuts import render,redirect

def home(request):
    return render(request, 'home.html')
def addProduct(request):
    return render(request, 'addProduct.html')
def editProduct(request):
    return render(request, 'editProduct.html')
def deleteProduct(request):
    return render(request, 'deleteProduct.html')
def productList(request):
    return render(request, 'productList.html')