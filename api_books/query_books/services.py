from api.services import get_books

def info_books(author):
    info_books = get_books(author=author)
    return info_books['books']