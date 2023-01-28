from django.shortcuts import render

def search(request):
    query = request.GET.get('q')
    # processar a pesquisa aqui
    return render(request, 'base.html', {'query': query})
    