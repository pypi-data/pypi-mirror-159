# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/sample/v1/helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'spaceone/api/sample/v1/helloworld.proto\x12\x16spaceone.api.sample.v1\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2e\n\nHelloWorld\x12W\n\tsay_hello\x12$.spaceone.api.sample.v1.HelloRequest\x1a\".spaceone.api.sample.v1.HelloReply\"\x00\x62\x06proto3')



_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLOREPLY = DESCRIPTOR.message_types_by_name['HelloReply']
HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'spaceone.api.sample.v1.helloworld_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.sample.v1.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'spaceone.api.sample.v1.helloworld_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.sample.v1.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

_HELLOWORLD = DESCRIPTOR.services_by_name['HelloWorld']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=67
  _HELLOREQUEST._serialized_end=95
  _HELLOREPLY._serialized_start=97
  _HELLOREPLY._serialized_end=126
  _HELLOWORLD._serialized_start=128
  _HELLOWORLD._serialized_end=229
# @@protoc_insertion_point(module_scope)
