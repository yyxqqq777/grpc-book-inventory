from inventory_client import InventoryClient

def get_book_titles(client, isbns):
    titles = []
    for isbn in isbns:
        book = client.get_book(isbn)
        titles.append(book.title)
    return titles


if __name__ == "__main__":
    # Create an instance of the gRPC client
    client = InventoryClient("localhost", 8082)

    # Call the get_book_titles function with two hardcoded ISBNs
    titles = get_book_titles(client, ["978-0984782857", "978-0439708180"])

    # Print the returned titles
    print(titles)
