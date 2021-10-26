from django.shortcuts import render

# importing function that obtains data about author to render
from .services import info_books

# Create your views here.


def query_books(request):

    # render the initial base template
    if request.method == 'GET':
        return render(request, 'query_books/base.html')

    # Render template with the information consulted
    if request.method == 'POST':

        # Obtaining the author's name to consult
        author = request.POST.get('author')

        # function that obtains data about author to render
        books = info_books(author)

        return render(request, 'query_books/result.html', {'info': books})
