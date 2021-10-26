from django.shortcuts import render

from .services import info_books

# Create your views here.


def query_books(request):
    if request.method == 'GET':
        return render(request, 'query_books/home.html')
    if request.method == 'POST':

        author = request.POST.get('author')
        books = info_books(author)

        return render(request, 'query_books/result.html', {'info': books})
