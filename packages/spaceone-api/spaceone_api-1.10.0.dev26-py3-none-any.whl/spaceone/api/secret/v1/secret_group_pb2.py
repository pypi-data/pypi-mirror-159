# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/secret/v1/secret_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2
from spaceone.api.secret.v1 import secret_pb2 as spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)spaceone/api/secret/v1/secret_group.proto\x12\x16spaceone.api.secret.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a#spaceone/api/secret/v1/secret.proto\"b\n\x18\x43reateSecretGroupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04tags\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"{\n\x18UpdateSecretGroupRequest\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x04 \x01(\t\"@\n\x12SecretGroupRequest\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"Q\n\x15GetSecretGroupRequest\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"Y\n\x18SecretGroupSecretRequest\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x11\n\tsecret_id\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"\x8b\x01\n\x10SecretGroupQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x17\n\x0fsecret_group_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tsecret_id\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"\xa7\x01\n\x15SecretGroupSecretInfo\x12\x42\n\x11secret_group_info\x18\x01 \x01(\x0b\x32\'.spaceone.api.secret.v1.SecretGroupInfo\x12\x37\n\x0bsecret_info\x18\x02 \x01(\x0b\x32\".spaceone.api.secret.v1.SecretInfo\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"\x86\x01\n\x0fSecretGroupInfo\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x05 \x01(\t\x12\x12\n\ncreated_at\x18\x06 \x01(\t\"a\n\x10SecretGroupsInfo\x12\x38\n\x07results\x18\x01 \x03(\x0b\x32\'.spaceone.api.secret.v1.SecretGroupInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"_\n\x14SecretGroupStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xa7\t\n\x0bSecretGroup\x12\x85\x01\n\x06\x63reate\x12\x30.spaceone.api.secret.v1.CreateSecretGroupRequest\x1a\'.spaceone.api.secret.v1.SecretGroupInfo\" \x82\xd3\xe4\x93\x02\x1a\"\x18/secret/v1/secret-groups\x12\x96\x01\n\x06update\x12\x30.spaceone.api.secret.v1.UpdateSecretGroupRequest\x1a\'.spaceone.api.secret.v1.SecretGroupInfo\"1\x82\xd3\xe4\x93\x02+\x1a)/secret/v1/secret-group/{secret_group_id}\x12\xa8\x01\n\nadd_secret\x12\x30.spaceone.api.secret.v1.SecretGroupSecretRequest\x1a-.spaceone.api.secret.v1.SecretGroupSecretInfo\"9\x82\xd3\xe4\x93\x02\x33\"1/secret/v1/secret-group/{secret_group_id}/secrets\x12\x9f\x01\n\rremove_secret\x12\x30.spaceone.api.secret.v1.SecretGroupSecretRequest\x1a\x16.google.protobuf.Empty\"D\x82\xd3\xe4\x93\x02>*</secret/v1/secret-group/{secret_group_id}/secret/{secret_id}\x12\x7f\n\x06\x64\x65lete\x12*.spaceone.api.secret.v1.SecretGroupRequest\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02+*)/secret/v1/secret-group/{secret_group_id}\x12\x90\x01\n\x03get\x12-.spaceone.api.secret.v1.GetSecretGroupRequest\x1a\'.spaceone.api.secret.v1.SecretGroupInfo\"1\x82\xd3\xe4\x93\x02+\x12)/secret/v1/secret-group/{secret_group_id}\x12\x9f\x01\n\x04list\x12(.spaceone.api.secret.v1.SecretGroupQuery\x1a(.spaceone.api.secret.v1.SecretGroupsInfo\"C\x82\xd3\xe4\x93\x02=\x12\x18/secret/v1/secret-groupsZ!\"\x1f/secret/v1/secret-groups/search\x12t\n\x04stat\x12,.spaceone.api.secret.v1.SecretGroupStatQuery\x1a\x17.google.protobuf.Struct\"%\x82\xd3\xe4\x93\x02\x1f\"\x1d/secret/v1/secret-groups/statb\x06proto3')



_CREATESECRETGROUPREQUEST = DESCRIPTOR.message_types_by_name['CreateSecretGroupRequest']
_UPDATESECRETGROUPREQUEST = DESCRIPTOR.message_types_by_name['UpdateSecretGroupRequest']
_SECRETGROUPREQUEST = DESCRIPTOR.message_types_by_name['SecretGroupRequest']
_GETSECRETGROUPREQUEST = DESCRIPTOR.message_types_by_name['GetSecretGroupRequest']
_SECRETGROUPSECRETREQUEST = DESCRIPTOR.message_types_by_name['SecretGroupSecretRequest']
_SECRETGROUPQUERY = DESCRIPTOR.message_types_by_name['SecretGroupQuery']
_SECRETGROUPSECRETINFO = DESCRIPTOR.message_types_by_name['SecretGroupSecretInfo']
_SECRETGROUPINFO = DESCRIPTOR.message_types_by_name['SecretGroupInfo']
_SECRETGROUPSINFO = DESCRIPTOR.message_types_by_name['SecretGroupsInfo']
_SECRETGROUPSTATQUERY = DESCRIPTOR.message_types_by_name['SecretGroupStatQuery']
CreateSecretGroupRequest = _reflection.GeneratedProtocolMessageType('CreateSecretGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESECRETGROUPREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.CreateSecretGroupRequest)
  })
_sym_db.RegisterMessage(CreateSecretGroupRequest)

UpdateSecretGroupRequest = _reflection.GeneratedProtocolMessageType('UpdateSecretGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESECRETGROUPREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.UpdateSecretGroupRequest)
  })
_sym_db.RegisterMessage(UpdateSecretGroupRequest)

SecretGroupRequest = _reflection.GeneratedProtocolMessageType('SecretGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupRequest)
  })
_sym_db.RegisterMessage(SecretGroupRequest)

GetSecretGroupRequest = _reflection.GeneratedProtocolMessageType('GetSecretGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSECRETGROUPREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.GetSecretGroupRequest)
  })
_sym_db.RegisterMessage(GetSecretGroupRequest)

SecretGroupSecretRequest = _reflection.GeneratedProtocolMessageType('SecretGroupSecretRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPSECRETREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupSecretRequest)
  })
_sym_db.RegisterMessage(SecretGroupSecretRequest)

SecretGroupQuery = _reflection.GeneratedProtocolMessageType('SecretGroupQuery', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPQUERY,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupQuery)
  })
_sym_db.RegisterMessage(SecretGroupQuery)

SecretGroupSecretInfo = _reflection.GeneratedProtocolMessageType('SecretGroupSecretInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPSECRETINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupSecretInfo)
  })
_sym_db.RegisterMessage(SecretGroupSecretInfo)

SecretGroupInfo = _reflection.GeneratedProtocolMessageType('SecretGroupInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupInfo)
  })
_sym_db.RegisterMessage(SecretGroupInfo)

SecretGroupsInfo = _reflection.GeneratedProtocolMessageType('SecretGroupsInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPSINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupsInfo)
  })
_sym_db.RegisterMessage(SecretGroupsInfo)

SecretGroupStatQuery = _reflection.GeneratedProtocolMessageType('SecretGroupStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPSTATQUERY,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupStatQuery)
  })
_sym_db.RegisterMessage(SecretGroupStatQuery)

_SECRETGROUP = DESCRIPTOR.services_by_name['SecretGroup']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SECRETGROUP.methods_by_name['create']._options = None
  _SECRETGROUP.methods_by_name['create']._serialized_options = b'\202\323\344\223\002\032\"\030/secret/v1/secret-groups'
  _SECRETGROUP.methods_by_name['update']._options = None
  _SECRETGROUP.methods_by_name['update']._serialized_options = b'\202\323\344\223\002+\032)/secret/v1/secret-group/{secret_group_id}'
  _SECRETGROUP.methods_by_name['add_secret']._options = None
  _SECRETGROUP.methods_by_name['add_secret']._serialized_options = b'\202\323\344\223\0023\"1/secret/v1/secret-group/{secret_group_id}/secrets'
  _SECRETGROUP.methods_by_name['remove_secret']._options = None
  _SECRETGROUP.methods_by_name['remove_secret']._serialized_options = b'\202\323\344\223\002>*</secret/v1/secret-group/{secret_group_id}/secret/{secret_id}'
  _SECRETGROUP.methods_by_name['delete']._options = None
  _SECRETGROUP.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002+*)/secret/v1/secret-group/{secret_group_id}'
  _SECRETGROUP.methods_by_name['get']._options = None
  _SECRETGROUP.methods_by_name['get']._serialized_options = b'\202\323\344\223\002+\022)/secret/v1/secret-group/{secret_group_id}'
  _SECRETGROUP.methods_by_name['list']._options = None
  _SECRETGROUP.methods_by_name['list']._serialized_options = b'\202\323\344\223\002=\022\030/secret/v1/secret-groupsZ!\"\037/secret/v1/secret-groups/search'
  _SECRETGROUP.methods_by_name['stat']._options = None
  _SECRETGROUP.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\037\"\035/secret/v1/secret-groups/stat'
  _CREATESECRETGROUPREQUEST._serialized_start=229
  _CREATESECRETGROUPREQUEST._serialized_end=327
  _UPDATESECRETGROUPREQUEST._serialized_start=329
  _UPDATESECRETGROUPREQUEST._serialized_end=452
  _SECRETGROUPREQUEST._serialized_start=454
  _SECRETGROUPREQUEST._serialized_end=518
  _GETSECRETGROUPREQUEST._serialized_start=520
  _GETSECRETGROUPREQUEST._serialized_end=601
  _SECRETGROUPSECRETREQUEST._serialized_start=603
  _SECRETGROUPSECRETREQUEST._serialized_end=692
  _SECRETGROUPQUERY._serialized_start=695
  _SECRETGROUPQUERY._serialized_end=834
  _SECRETGROUPSECRETINFO._serialized_start=837
  _SECRETGROUPSECRETINFO._serialized_end=1004
  _SECRETGROUPINFO._serialized_start=1007
  _SECRETGROUPINFO._serialized_end=1141
  _SECRETGROUPSINFO._serialized_start=1143
  _SECRETGROUPSINFO._serialized_end=1240
  _SECRETGROUPSTATQUERY._serialized_start=1242
  _SECRETGROUPSTATQUERY._serialized_end=1337
  _SECRETGROUP._serialized_start=1340
  _SECRETGROUP._serialized_end=2531
# @@protoc_insertion_point(module_scope)
