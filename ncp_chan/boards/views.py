from django.shortcuts import render
from .models import Thread, Reply

def home(request):
    return render(request, 'home/home.html')

def wel(request):
    context = {
        'board': {
            'extension': '/wel/',
            'description': 'Welcome/Introductions'
        },
        'threads': {
            'thread_id': {
                'title': 'title',
                'author': 'author',
                'date': 'date',
                'content': 'content',
                'replies': {
                    'reply_id': {
                        'author': 'author',
                        'date': 'date',
                        'content': 'content'
                    }
                }
            }
        }
    }
    threads_context = context['threads']
    threads = Thread.objects.all()

    for thread in threads:
        threads_context[str(thread.id)] = {
            'title': thread.title,
            'author': thread.author,
            'date': thread.date,
            'content': thread.content,
            'replies': {}
        }
        replies = thread.reply_set.all()
        for reply in replies:
            threads_context[str(thread.id)]['replies'][str(reply.id)] = {
                'author': reply.author,
                'date': reply.date,
                'content': reply.content
            }
    
    return render(request, 'boards/wel.html', context)