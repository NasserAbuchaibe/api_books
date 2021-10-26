# Importing function that makes the query and filters the data
from api.services import get_books


def info_books(author):
    """[Get filtered and organized data about the author]

    Args:
        author ([str]): [Author name]

    Returns:
        [list]: [list with author data to render]
    """
    # function that makes the query and filters the data
    info_books = get_books(author=author)

    return info_books['books']
