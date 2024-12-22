from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'data': 'This is a placeholder for index page'
    }
    return render(request, 'index.html', context=context)


def result(request):
    context = {
        'data': 'This is a placeholder for result page'
    }
    return render(request, 'result.html', context=context)


def detail(request):
    context = {
        'data': 'This is a placeholder for detail page'
    }
    return render(request, 'detail.html', context=context)