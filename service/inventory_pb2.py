# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import book_pb2 as book__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\x1a\nbook.proto\"#\n\x0c\x42ookResponse\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book\"\x1b\n\x0b\x42ookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"%\n\x12\x43reateBookResponse\x12\x0f\n\x07success\x18\x01 \x01(\t2`\n\x10InventoryService\x12*\n\nCreateBook\x12\x05.Book\x1a\x13.CreateBookResponse\"\x00\x12 \n\x07GetBook\x12\x0c.BookRequest\x1a\x05.Book\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOKRESPONSE._serialized_start=31
  _BOOKRESPONSE._serialized_end=66
  _BOOKREQUEST._serialized_start=68
  _BOOKREQUEST._serialized_end=95
  _CREATEBOOKRESPONSE._serialized_start=97
  _CREATEBOOKRESPONSE._serialized_end=134
  _INVENTORYSERVICE._serialized_start=136
  _INVENTORYSERVICE._serialized_end=232
# @@protoc_insertion_point(module_scope)
