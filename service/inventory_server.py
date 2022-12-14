from concurrent import futures

import grpc

import book_pb2
import inventory_pb2
import inventory_pb2_grpc


class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
    def __init__(self):
        book1 = book_pb2.Book(title="Cracking the Coding Interview", isbn="978-0984782857", genre=book_pb2.Genre.FAIRY_TALE, author="Gayle Laakmann McDowell", publishing_year=2015)
        book2 = book_pb2.Book(title="Harry Potter and the Sorcerer's Stone", isbn="978-0439708180", genre=book_pb2.Genre.NOVEL, author="J.K. Rowling", publishing_year=1998)
        self.books = [book1, book2]


    def CreateBook(self, request, context):
        print(request)
        self.books.append(request)
        return inventory_pb2.BookResponse()

    def GetBook(self, request, context):
        isbn = request.value
        print(isbn)
        for b in self.books:
            if b.isbn == isbn:
                return b

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryService(), server)
    server.add_insecure_port('localhost:8082')
    server.start()
    print("server start")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()