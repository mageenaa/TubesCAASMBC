from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul' : 'Tugas Besar',
        'lab' : 'MBC Laboratory',
    }
    return render(request, 'index.html', context)

def counter(request):
    text = request.POST['text']
    total_kata = len(text.split())
    return render(request, 'counter.html', {'total_kata' : total_kata})