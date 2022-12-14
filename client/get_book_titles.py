from inventory_client import InventoryClient

def get_book_titles(client, isbns):
    res = []
    for isbn in isbns:
        book = client.get_book(isbn)
        res.append(book.title)
    return res


if __name__ == "__main__":
    # Create an instance of InventoryClient
    client = InventoryClient("localhost", 8082)

    # Call the function with hardcoded ISBNs
    titles = get_book_titles(client, ["978-0984782857", "978-0439708180"])

    print(titles)
