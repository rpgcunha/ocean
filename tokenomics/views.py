from django.shortcuts import render

def ocean(request):
    return render(request, 'tokenomics/$ocean.html')

def cardsDetails(request):
    return render(request, 'tokenomics/royalty-cards-details.html')

def distribution(request):
    return render(request, 'tokenomics/token-distribution.html')

def contracts(request):
    return render(request, 'tokenomics/contracts.html')
