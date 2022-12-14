
import grpc
import sys
sys.path.insert(0, '/Users/yunxuan/Desktop/f22/api_design/hw/a3/service')
import inventory_pb2_grpc
import inventory_pb2

class InventoryClient:
    def __init__(self, server_address, port):
        self.channel = grpc.insecure_channel(f"{server_address}:{port}")
        self.stub = inventory_pb2_grpc.InventoryServiceStub(self.channel)

    def get_book(self, isbn):
        # print("isbn is " + isbn)
        request = inventory_pb2.BookRequest(isbn=isbn)
        return self.stub.GetBook(request)

