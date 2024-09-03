from django.shortcuts import render

def landing_page(request):
    return render(request, 'index.html')

def oil_page(request):
    return render(request, 'oil.html')


def spices_page(request):
    return render(request, 'spices.html')

def honey_page(request):
    return render(request, 'honey.html')

def bulk_page(request):
    return render(request, 'bulk.html')

def retail_page(request):
    return render(request, 'retail.html')


def pro_page(request):
    return render(request, 'honeyproduct.html')


def beewax_page(request):
    return render(request, 'beewax.html')


def candel_page(request):
    return render(request, 'candel.html')


def coc_page(request):
    return render(request, 'cocount.html')