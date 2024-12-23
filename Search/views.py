from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'data': 'This is a placeholder for index page'
    }
    return render(request, 'index.html', context=context)


def result(request):
    query = request.GET.get('query', '') 

    if (query == None) or (query == ''):
        return render(request, 'index.html')

    context = {
        'query': query,
    }
    return render(request, 'result.html', context=context)


def detail(request):
    query = request.GET.get('query', '') 

    if (query == None) or (query == ''):
        return render(request, 'index.html')

    context = {
        'query': query,
    }
    return render(request, 'detail.html', context=context)