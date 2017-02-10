from django.shortcuts import render


def index(request):
    data = {'mydata': "Roll Tide!"}
    return render(request, 'blog/index.html', data)
# Create your views here.
