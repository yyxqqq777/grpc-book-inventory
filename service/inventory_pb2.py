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


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import book_pb2 as book__pb2
import inventoryItem_pb2 as inventoryItem__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\nbook.proto\x1a\x13inventoryItem.proto2s\n\x10InventoryService\x12-\n\nCreateBook\x12\x05.Book\x1a\x16.google.protobuf.Empty\"\x00\x12\x30\n\x07GetBook\x12\x1c.google.protobuf.StringValue\x1a\x05.Book\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INVENTORYSERVICE._serialized_start=113
  _INVENTORYSERVICE._serialized_end=228
# @@protoc_insertion_point(module_scope)