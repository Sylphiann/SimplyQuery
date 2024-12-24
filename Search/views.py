from django.shortcuts import render
from retrieve.retriever import Retriever
# from .dummy import get_result, get_data_by_docno

# Create your views here.

def index(request):
    context = {
        'data': 'This is a placeholder for index page'
    }
    return render(request, 'index.html', context=context)


def result(request):
    query = request.GET.get('query', '')
    retr = Retriever()

    if (query == None) or (query == ''):
        return render(request, 'index.html')

    context = {
        'query': query,
        'results': retr.get_serp(query)
    }
    return render(request, 'result.html', context=context)


def detail(request):
    query = request.GET.get('query', '')
    retr = Retriever()

    if (query == None) or (query == ''):
        return render(request, 'index.html')
    
    content = retr.get_data_by_docno(query)

    context = {
        'query': query,
        'title': content["title"],
        'content': content["content"]
    }
    return render(request, 'detail.html', context=context)