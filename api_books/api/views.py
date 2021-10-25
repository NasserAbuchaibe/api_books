from django.http import JsonResponse
from rest_framework.views import APIView

from .services import get_books

# Create your views here.


class BooksView(APIView):
    def get(self, request):
        author = request.data.get('author')

        info_books = get_books(author=author)

        return JsonResponse(info_books)
