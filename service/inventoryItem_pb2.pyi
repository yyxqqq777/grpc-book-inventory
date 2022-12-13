import book_pb2 as _book_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

AVAILABLE: Status
DESCRIPTOR: _descriptor.FileDescriptor
TAKEN: Status

class InventoryItem(_message.Message):
    __slots__ = ["book", "id", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: _book_pb2.Book
    id: int
    status: Status
    def __init__(self, id: _Optional[int] = ..., book: _Optional[_Union[_book_pb2.Book, _Mapping]] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
