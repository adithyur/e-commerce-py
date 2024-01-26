from django.shortcuts import render
from productapp.models import Product
from django.db.models import Q

def SearchResult(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = None

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search_results.html', context)
