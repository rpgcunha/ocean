from django.shortcuts import render

def betting(request):
    return render(request, 'products/betting-security.html')

def preSale(request):
    return render(request, 'products/pre-sale.html')

def token(request):
    return render(request, 'products/token.html')

def cards(request):
    return render(request, 'products/royalty-cards.html')

def market(request):
    return render(request, 'products/market-place.html')

def roadMap(request):
    return render(request, 'products/road-map.html')

def modes(request):
    return render(request, 'products/available-betting-modes.html')
    