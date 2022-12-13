from concurrent import futures

import grpc

import book_pb2
import inventory_pb2
import inventory_pb2_grpc


class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
    def __init__(self):
        self.books = {}

    def CreateBook(self, request, context):
        pass

    def GetBook(self, request, context):
        pass

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  inventory_pb2_grpc.add_InventoryServiceServicer_to_server(
      InventoryService(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()