from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def wel(request):
    context = {
        'board': {
            'extension': '/wel/',
            'description': 'Welcome/Introductions'
        }
    }
    return render(request, 'boards/wel.html', context)