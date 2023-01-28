from django.shortcuts import render

def media(request):
    return render(request, 'extras/social-media.html')