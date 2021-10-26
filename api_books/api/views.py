from django.http import JsonResponse
from rest_framework.views import APIView

# Importing function that makes the query and filters the data
from .services import get_books

# Create your views here.


class BooksView(APIView):
    """[endpoint]
    """

    def get(self, request):
        # Obtaining the author's name to consult
        author = request.data.get('author')

        # function that makes the query and filters the data
        info_books = get_books(author=author)

        # Return the data in JSON format
        return JsonResponse(info_books)
