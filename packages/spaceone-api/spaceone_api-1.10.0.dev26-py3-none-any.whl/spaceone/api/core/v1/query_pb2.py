# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/core/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n spaceone/api/core/v1/query.proto\x12\x14spaceone.api.core.v1\x1a\x1cgoogle/protobuf/struct.proto\"\xc1\x01\n\x06\x46ilter\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12\x0b\n\x01k\x18\x02 \x01(\tH\x00\x12\'\n\x05value\x18\x03 \x01(\x0b\x32\x16.google.protobuf.ValueH\x01\x12#\n\x01v\x18\x04 \x01(\x0b\x32\x16.google.protobuf.ValueH\x01\x12\x12\n\x08operator\x18\x05 \x01(\tH\x02\x12\x0b\n\x01o\x18\x06 \x01(\tH\x02\x42\x0b\n\tkey_aliasB\r\n\x0bvalue_aliasB\x10\n\x0eoperator_alias\"$\n\x07SortKey\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\x08\"N\n\x04Sort\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\x08\x12+\n\x04keys\x18\x03 \x03(\x0b\x32\x1d.spaceone.api.core.v1.SortKey\"$\n\x04Page\x12\r\n\x05start\x18\x01 \x01(\r\x12\r\n\x05limit\x18\x02 \x01(\r\"\xfe\x01\n\x05Query\x12,\n\x06\x66ilter\x18\x01 \x03(\x0b\x32\x1c.spaceone.api.core.v1.Filter\x12/\n\tfilter_or\x18\x02 \x03(\x0b\x32\x1c.spaceone.api.core.v1.Filter\x12(\n\x04sort\x18\x03 \x01(\x0b\x32\x1a.spaceone.api.core.v1.Sort\x12(\n\x04page\x18\x04 \x01(\x0b\x32\x1a.spaceone.api.core.v1.Page\x12\x0f\n\x07minimal\x18\x05 \x01(\x08\x12\x12\n\ncount_only\x18\x06 \x01(\x08\x12\x0c\n\x04only\x18\x07 \x03(\t\x12\x0f\n\x07keyword\x18\x08 \x01(\t\"|\n\x11\x41ggregateGroupKey\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12\x0b\n\x01k\x18\x02 \x01(\tH\x00\x12\x0e\n\x04name\x18\x03 \x01(\tH\x01\x12\x0b\n\x01n\x18\x04 \x01(\tH\x01\x12\x13\n\x0b\x64\x61te_format\x18\x05 \x01(\tB\x0b\n\tkey_aliasB\x0c\n\nname_alias\"l\n\x16\x41ggregateGroupSubField\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12\x0b\n\x01k\x18\x02 \x01(\tH\x00\x12\x0e\n\x04name\x18\x03 \x01(\tH\x01\x12\x0b\n\x01n\x18\x04 \x01(\tH\x01\x42\x0b\n\tkey_aliasB\x0c\n\nname_alias\"\xd0\x01\n\x15\x41ggregateSubCondition\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12\x0b\n\x01k\x18\x02 \x01(\tH\x00\x12\'\n\x05value\x18\x03 \x01(\x0b\x32\x16.google.protobuf.ValueH\x01\x12#\n\x01v\x18\x04 \x01(\x0b\x32\x16.google.protobuf.ValueH\x01\x12\x12\n\x08operator\x18\x05 \x01(\tH\x02\x12\x0b\n\x01o\x18\x06 \x01(\tH\x02\x42\x0b\n\tkey_aliasB\r\n\x0bvalue_aliasB\x10\n\x0eoperator_alias\"\x9b\x02\n\x13\x41ggregateGroupField\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12\x0b\n\x01k\x18\x02 \x01(\tH\x00\x12\x0e\n\x04name\x18\x03 \x01(\tH\x01\x12\x0b\n\x01n\x18\x04 \x01(\tH\x01\x12\x12\n\x08operator\x18\x05 \x01(\tH\x02\x12\x0b\n\x01o\x18\x06 \x01(\tH\x02\x12<\n\x06\x66ields\x18\x07 \x03(\x0b\x32,.spaceone.api.core.v1.AggregateGroupSubField\x12?\n\nconditions\x18\x08 \x03(\x0b\x32+.spaceone.api.core.v1.AggregateSubConditionB\x0b\n\tkey_aliasB\x0c\n\nname_aliasB\x10\n\x0eoperator_alias\"\x82\x01\n\x0e\x41ggregateGroup\x12\x35\n\x04keys\x18\x01 \x03(\x0b\x32\'.spaceone.api.core.v1.AggregateGroupKey\x12\x39\n\x06\x66ields\x18\x02 \x03(\x0b\x32).spaceone.api.core.v1.AggregateGroupField\"\x9e\x01\n\x15\x41ggregateProjectField\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12\x0b\n\x01k\x18\x02 \x01(\tH\x00\x12\x0e\n\x04name\x18\x03 \x01(\tH\x01\x12\x0b\n\x01n\x18\x04 \x01(\tH\x01\x12\x12\n\x08operator\x18\x05 \x01(\tH\x02\x12\x0b\n\x01o\x18\x06 \x01(\tH\x02\x42\x0b\n\tkey_aliasB\x0c\n\nname_aliasB\x10\n\x0eoperator_alias\"e\n\x10\x41ggregateProject\x12;\n\x06\x66ields\x18\x01 \x03(\x0b\x32+.spaceone.api.core.v1.AggregateProjectField\x12\x14\n\x0c\x65xclude_keys\x18\x02 \x01(\x08\"\x1f\n\x0f\x41ggregateUnwind\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x1e\n\x0e\x41ggregateCount\x12\x0c\n\x04name\x18\x01 \x01(\t\"W\n\rAggregateSort\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\x08\x12+\n\x04keys\x18\x03 \x03(\x0b\x32\x1d.spaceone.api.core.v1.SortKey\"\xe0\x02\n\x13StatisticsAggregate\x12\x37\n\x06unwind\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.AggregateUnwindH\x00\x12\x35\n\x05group\x18\x02 \x01(\x0b\x32$.spaceone.api.core.v1.AggregateGroupH\x00\x12\x35\n\x05\x63ount\x18\x03 \x01(\x0b\x32$.spaceone.api.core.v1.AggregateCountH\x00\x12\x33\n\x04sort\x18\x04 \x01(\x0b\x32#.spaceone.api.core.v1.AggregateSortH\x00\x12\x39\n\x07project\x18\x05 \x01(\x0b\x32&.spaceone.api.core.v1.AggregateProjectH\x00\x12\x0f\n\x05limit\x18\x06 \x01(\x05H\x00\x12\x0e\n\x04skip\x18\x07 \x01(\x05H\x00\x42\x11\n\x0f\x61ggregate_alias\"\xfb\x01\n\x0fStatisticsQuery\x12,\n\x06\x66ilter\x18\x01 \x03(\x0b\x32\x1c.spaceone.api.core.v1.Filter\x12/\n\tfilter_or\x18\x02 \x03(\x0b\x32\x1c.spaceone.api.core.v1.Filter\x12<\n\taggregate\x18\x03 \x03(\x0b\x32).spaceone.api.core.v1.StatisticsAggregate\x12(\n\x04page\x18\x04 \x01(\x0b\x32\x1a.spaceone.api.core.v1.Page\x12\x10\n\x08\x64istinct\x18\x05 \x01(\t\x12\x0f\n\x07keyword\x18\x06 \x01(\tb\x06proto3')



_FILTER = DESCRIPTOR.message_types_by_name['Filter']
_SORTKEY = DESCRIPTOR.message_types_by_name['SortKey']
_SORT = DESCRIPTOR.message_types_by_name['Sort']
_PAGE = DESCRIPTOR.message_types_by_name['Page']
_QUERY = DESCRIPTOR.message_types_by_name['Query']
_AGGREGATEGROUPKEY = DESCRIPTOR.message_types_by_name['AggregateGroupKey']
_AGGREGATEGROUPSUBFIELD = DESCRIPTOR.message_types_by_name['AggregateGroupSubField']
_AGGREGATESUBCONDITION = DESCRIPTOR.message_types_by_name['AggregateSubCondition']
_AGGREGATEGROUPFIELD = DESCRIPTOR.message_types_by_name['AggregateGroupField']
_AGGREGATEGROUP = DESCRIPTOR.message_types_by_name['AggregateGroup']
_AGGREGATEPROJECTFIELD = DESCRIPTOR.message_types_by_name['AggregateProjectField']
_AGGREGATEPROJECT = DESCRIPTOR.message_types_by_name['AggregateProject']
_AGGREGATEUNWIND = DESCRIPTOR.message_types_by_name['AggregateUnwind']
_AGGREGATECOUNT = DESCRIPTOR.message_types_by_name['AggregateCount']
_AGGREGATESORT = DESCRIPTOR.message_types_by_name['AggregateSort']
_STATISTICSAGGREGATE = DESCRIPTOR.message_types_by_name['StatisticsAggregate']
_STATISTICSQUERY = DESCRIPTOR.message_types_by_name['StatisticsQuery']
Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
  'DESCRIPTOR' : _FILTER,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.Filter)
  })
_sym_db.RegisterMessage(Filter)

SortKey = _reflection.GeneratedProtocolMessageType('SortKey', (_message.Message,), {
  'DESCRIPTOR' : _SORTKEY,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.SortKey)
  })
_sym_db.RegisterMessage(SortKey)

Sort = _reflection.GeneratedProtocolMessageType('Sort', (_message.Message,), {
  'DESCRIPTOR' : _SORT,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.Sort)
  })
_sym_db.RegisterMessage(Sort)

Page = _reflection.GeneratedProtocolMessageType('Page', (_message.Message,), {
  'DESCRIPTOR' : _PAGE,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.Page)
  })
_sym_db.RegisterMessage(Page)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.Query)
  })
_sym_db.RegisterMessage(Query)

AggregateGroupKey = _reflection.GeneratedProtocolMessageType('AggregateGroupKey', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEGROUPKEY,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateGroupKey)
  })
_sym_db.RegisterMessage(AggregateGroupKey)

AggregateGroupSubField = _reflection.GeneratedProtocolMessageType('AggregateGroupSubField', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEGROUPSUBFIELD,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateGroupSubField)
  })
_sym_db.RegisterMessage(AggregateGroupSubField)

AggregateSubCondition = _reflection.GeneratedProtocolMessageType('AggregateSubCondition', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATESUBCONDITION,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateSubCondition)
  })
_sym_db.RegisterMessage(AggregateSubCondition)

AggregateGroupField = _reflection.GeneratedProtocolMessageType('AggregateGroupField', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEGROUPFIELD,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateGroupField)
  })
_sym_db.RegisterMessage(AggregateGroupField)

AggregateGroup = _reflection.GeneratedProtocolMessageType('AggregateGroup', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEGROUP,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateGroup)
  })
_sym_db.RegisterMessage(AggregateGroup)

AggregateProjectField = _reflection.GeneratedProtocolMessageType('AggregateProjectField', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEPROJECTFIELD,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateProjectField)
  })
_sym_db.RegisterMessage(AggregateProjectField)

AggregateProject = _reflection.GeneratedProtocolMessageType('AggregateProject', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEPROJECT,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateProject)
  })
_sym_db.RegisterMessage(AggregateProject)

AggregateUnwind = _reflection.GeneratedProtocolMessageType('AggregateUnwind', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEUNWIND,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateUnwind)
  })
_sym_db.RegisterMessage(AggregateUnwind)

AggregateCount = _reflection.GeneratedProtocolMessageType('AggregateCount', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATECOUNT,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateCount)
  })
_sym_db.RegisterMessage(AggregateCount)

AggregateSort = _reflection.GeneratedProtocolMessageType('AggregateSort', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATESORT,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.AggregateSort)
  })
_sym_db.RegisterMessage(AggregateSort)

StatisticsAggregate = _reflection.GeneratedProtocolMessageType('StatisticsAggregate', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICSAGGREGATE,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.StatisticsAggregate)
  })
_sym_db.RegisterMessage(StatisticsAggregate)

StatisticsQuery = _reflection.GeneratedProtocolMessageType('StatisticsQuery', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICSQUERY,
  '__module__' : 'spaceone.api.core.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.core.v1.StatisticsQuery)
  })
_sym_db.RegisterMessage(StatisticsQuery)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILTER._serialized_start=89
  _FILTER._serialized_end=282
  _SORTKEY._serialized_start=284
  _SORTKEY._serialized_end=320
  _SORT._serialized_start=322
  _SORT._serialized_end=400
  _PAGE._serialized_start=402
  _PAGE._serialized_end=438
  _QUERY._serialized_start=441
  _QUERY._serialized_end=695
  _AGGREGATEGROUPKEY._serialized_start=697
  _AGGREGATEGROUPKEY._serialized_end=821
  _AGGREGATEGROUPSUBFIELD._serialized_start=823
  _AGGREGATEGROUPSUBFIELD._serialized_end=931
  _AGGREGATESUBCONDITION._serialized_start=934
  _AGGREGATESUBCONDITION._serialized_end=1142
  _AGGREGATEGROUPFIELD._serialized_start=1145
  _AGGREGATEGROUPFIELD._serialized_end=1428
  _AGGREGATEGROUP._serialized_start=1431
  _AGGREGATEGROUP._serialized_end=1561
  _AGGREGATEPROJECTFIELD._serialized_start=1564
  _AGGREGATEPROJECTFIELD._serialized_end=1722
  _AGGREGATEPROJECT._serialized_start=1724
  _AGGREGATEPROJECT._serialized_end=1825
  _AGGREGATEUNWIND._serialized_start=1827
  _AGGREGATEUNWIND._serialized_end=1858
  _AGGREGATECOUNT._serialized_start=1860
  _AGGREGATECOUNT._serialized_end=1890
  _AGGREGATESORT._serialized_start=1892
  _AGGREGATESORT._serialized_end=1979
  _STATISTICSAGGREGATE._serialized_start=1982
  _STATISTICSAGGREGATE._serialized_end=2334
  _STATISTICSQUERY._serialized_start=2337
  _STATISTICSQUERY._serialized_end=2588
# @@protoc_insertion_point(module_scope)
