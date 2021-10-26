import requests

# api endpoint
url = 'https://www.googleapis.com/books/v1/volumes'


def get_books(author):
    """[Consult the endpoint of the google books api
        and filter and organize the data]

    Args:
        author ([str]): [Author name]

    Returns:
        [dict]: [Information about the author's books or books about the
                author or the status code if the request fails]
    """
    queries = {'q': author}
    response = requests.get(url, params=queries)
    
    # Filter and organize the received data
    if response.status_code == 200:
        data = response.json()
        info_books = data = data['items']
        books = []
        for book in info_books:
            book_dict = {
                'title': book['volumeInfo']['title'],
                'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
                'publishedDate': book['volumeInfo']['publishedDate'] if 'publishedDate' in book['volumeInfo'] else "",
            }
            books.append(book_dict)
        dict_books = {}
        dict_books['books'] = books
        return dict_books

    return {'Status code': response.status_code}
