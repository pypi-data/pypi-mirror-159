# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v1/project.proto
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
from spaceone.api.identity.v1 import role_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2
from spaceone.api.identity.v1 import project_group_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_project__group__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&spaceone/api/identity/v1/project.proto\x12\x18spaceone.api.identity.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a#spaceone/api/identity/v1/role.proto\x1a,spaceone/api/identity/v1/project_group.proto\"x\n\x14\x43reateProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10project_group_id\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x04 \x01(\t\"\x8c\x01\n\x14UpdateProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x10project_group_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"7\n\x0eProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"H\n\x11GetProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\x9a\x01\n\x0cProjectQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x18\n\x10project_group_id\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\t\x12\x11\n\tdomain_id\x18\x06 \x01(\t\"\xd9\x01\n\x0bProjectInfo\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x46\n\x12project_group_info\x18\x04 \x01(\x0b\x32*.spaceone.api.identity.v1.ProjectGroupInfo\x12\x11\n\tdomain_id\x18\x0b \x01(\t\x12\x12\n\ncreated_by\x18\x15 \x01(\t\x12\x12\n\ncreated_at\x18\x16 \x01(\t\"[\n\x0cProjectsInfo\x12\x36\n\x07results\x18\x01 \x03(\x0b\x32%.spaceone.api.identity.v1.ProjectInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"\xcf\x01\n\x17\x41\x64\x64ProjectMemberRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0f\n\x07role_id\x18\x03 \x01(\t\x12*\n\x06labels\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x06 \x01(\t\x12\x18\n\x10is_external_user\x18\x07 \x01(\x08\"\xa7\x01\n\x1aModifyProjectMemberRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12*\n\x06labels\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"T\n\x1aRemoveProjectMemberRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"\xa8\x01\n\x12ProjectMemberQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0f\n\x07role_id\x18\x04 \x01(\t\x12\x1d\n\x15include_parent_member\x18\x05 \x01(\x08\x12\x11\n\tdomain_id\x18\x06 \x01(\t\"\x93\x03\n\x16ProjectRoleBindingInfo\x12\x17\n\x0frole_binding_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x13\n\x0bresource_id\x18\x03 \x01(\t\x12\x35\n\trole_info\x18\x04 \x01(\x0b\x32\".spaceone.api.identity.v1.RoleInfo\x12;\n\x0cproject_info\x18\x05 \x01(\x0b\x32%.spaceone.api.identity.v1.ProjectInfo\x12\x46\n\x12project_group_info\x18\x06 \x01(\x0b\x32*.spaceone.api.identity.v1.ProjectGroupInfo\x12*\n\x06labels\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x0b \x01(\t\x12\x12\n\ncreated_at\x18\x15 \x01(\t\"q\n\x17ProjectRoleBindingsInfo\x12\x41\n\x07results\x18\x01 \x03(\x0b\x32\x30.spaceone.api.identity.v1.ProjectRoleBindingInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"[\n\x10ProjectStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xef\x0b\n\x07Project\x12~\n\x06\x63reate\x12..spaceone.api.identity.v1.CreateProjectRequest\x1a%.spaceone.api.identity.v1.ProjectInfo\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/identity/v1/projects\x12\x8a\x01\n\x06update\x12..spaceone.api.identity.v1.UpdateProjectRequest\x1a%.spaceone.api.identity.v1.ProjectInfo\")\x82\xd3\xe4\x93\x02#\x1a!/identity/v1/project/{project_id}\x12u\n\x06\x64\x65lete\x12(.spaceone.api.identity.v1.ProjectRequest\x1a\x16.google.protobuf.Empty\")\x82\xd3\xe4\x93\x02#*!/identity/v1/project/{project_id}\x12\x84\x01\n\x03get\x12+.spaceone.api.identity.v1.GetProjectRequest\x1a%.spaceone.api.identity.v1.ProjectInfo\")\x82\xd3\xe4\x93\x02#\x12!/identity/v1/project/{project_id}\x12\x95\x01\n\x04list\x12&.spaceone.api.identity.v1.ProjectQuery\x1a&.spaceone.api.identity.v1.ProjectsInfo\"=\x82\xd3\xe4\x93\x02\x37\x12\x15/identity/v1/projectsZ\x1e\"\x1c/identity/v1/projects/search\x12o\n\x04stat\x12*.spaceone.api.identity.v1.ProjectStatQuery\x1a\x17.google.protobuf.Struct\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/identity/v1/projects/stat\x12\xa4\x01\n\nadd_member\x12\x31.spaceone.api.identity.v1.AddProjectMemberRequest\x1a\x30.spaceone.api.identity.v1.ProjectRoleBindingInfo\"1\x82\xd3\xe4\x93\x02+\")/identity/v1/project/{project_id}/members\x12\xb3\x01\n\rmodify_member\x12\x34.spaceone.api.identity.v1.ModifyProjectMemberRequest\x1a\x30.spaceone.api.identity.v1.ProjectRoleBindingInfo\":\x82\xd3\xe4\x93\x02\x34\x1a\x32/identity/v1/project/{project_id}/member/{user_id}\x12\x99\x01\n\rremove_member\x12\x34.spaceone.api.identity.v1.RemoveProjectMemberRequest\x1a\x16.google.protobuf.Empty\":\x82\xd3\xe4\x93\x02\x34*2/identity/v1/project/{project_id}/member/{user_id}\x12\xd6\x01\n\x0clist_members\x12,.spaceone.api.identity.v1.ProjectMemberQuery\x1a\x31.spaceone.api.identity.v1.ProjectRoleBindingsInfo\"e\x82\xd3\xe4\x93\x02_\x12)/identity/v1/project/{project_id}/membersZ2\"0/identity/v1/project/{project_id}/members/searchb\x06proto3')



_CREATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['CreateProjectRequest']
_UPDATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UpdateProjectRequest']
_PROJECTREQUEST = DESCRIPTOR.message_types_by_name['ProjectRequest']
_GETPROJECTREQUEST = DESCRIPTOR.message_types_by_name['GetProjectRequest']
_PROJECTQUERY = DESCRIPTOR.message_types_by_name['ProjectQuery']
_PROJECTINFO = DESCRIPTOR.message_types_by_name['ProjectInfo']
_PROJECTSINFO = DESCRIPTOR.message_types_by_name['ProjectsInfo']
_ADDPROJECTMEMBERREQUEST = DESCRIPTOR.message_types_by_name['AddProjectMemberRequest']
_MODIFYPROJECTMEMBERREQUEST = DESCRIPTOR.message_types_by_name['ModifyProjectMemberRequest']
_REMOVEPROJECTMEMBERREQUEST = DESCRIPTOR.message_types_by_name['RemoveProjectMemberRequest']
_PROJECTMEMBERQUERY = DESCRIPTOR.message_types_by_name['ProjectMemberQuery']
_PROJECTROLEBINDINGINFO = DESCRIPTOR.message_types_by_name['ProjectRoleBindingInfo']
_PROJECTROLEBINDINGSINFO = DESCRIPTOR.message_types_by_name['ProjectRoleBindingsInfo']
_PROJECTSTATQUERY = DESCRIPTOR.message_types_by_name['ProjectStatQuery']
CreateProjectRequest = _reflection.GeneratedProtocolMessageType('CreateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTREQUEST,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.CreateProjectRequest)
  })
_sym_db.RegisterMessage(CreateProjectRequest)

UpdateProjectRequest = _reflection.GeneratedProtocolMessageType('UpdateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROJECTREQUEST,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UpdateProjectRequest)
  })
_sym_db.RegisterMessage(UpdateProjectRequest)

ProjectRequest = _reflection.GeneratedProtocolMessageType('ProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTREQUEST,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ProjectRequest)
  })
_sym_db.RegisterMessage(ProjectRequest)

GetProjectRequest = _reflection.GeneratedProtocolMessageType('GetProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTREQUEST,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.GetProjectRequest)
  })
_sym_db.RegisterMessage(GetProjectRequest)

ProjectQuery = _reflection.GeneratedProtocolMessageType('ProjectQuery', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTQUERY,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ProjectQuery)
  })
_sym_db.RegisterMessage(ProjectQuery)

ProjectInfo = _reflection.GeneratedProtocolMessageType('ProjectInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTINFO,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ProjectInfo)
  })
_sym_db.RegisterMessage(ProjectInfo)

ProjectsInfo = _reflection.GeneratedProtocolMessageType('ProjectsInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTSINFO,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ProjectsInfo)
  })
_sym_db.RegisterMessage(ProjectsInfo)

AddProjectMemberRequest = _reflection.GeneratedProtocolMessageType('AddProjectMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDPROJECTMEMBERREQUEST,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.AddProjectMemberRequest)
  })
_sym_db.RegisterMessage(AddProjectMemberRequest)

ModifyProjectMemberRequest = _reflection.GeneratedProtocolMessageType('ModifyProjectMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYPROJECTMEMBERREQUEST,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ModifyProjectMemberRequest)
  })
_sym_db.RegisterMessage(ModifyProjectMemberRequest)

RemoveProjectMemberRequest = _reflection.GeneratedProtocolMessageType('RemoveProjectMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPROJECTMEMBERREQUEST,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RemoveProjectMemberRequest)
  })
_sym_db.RegisterMessage(RemoveProjectMemberRequest)

ProjectMemberQuery = _reflection.GeneratedProtocolMessageType('ProjectMemberQuery', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTMEMBERQUERY,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ProjectMemberQuery)
  })
_sym_db.RegisterMessage(ProjectMemberQuery)

ProjectRoleBindingInfo = _reflection.GeneratedProtocolMessageType('ProjectRoleBindingInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTROLEBINDINGINFO,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ProjectRoleBindingInfo)
  })
_sym_db.RegisterMessage(ProjectRoleBindingInfo)

ProjectRoleBindingsInfo = _reflection.GeneratedProtocolMessageType('ProjectRoleBindingsInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTROLEBINDINGSINFO,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ProjectRoleBindingsInfo)
  })
_sym_db.RegisterMessage(ProjectRoleBindingsInfo)

ProjectStatQuery = _reflection.GeneratedProtocolMessageType('ProjectStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTSTATQUERY,
  '__module__' : 'spaceone.api.identity.v1.project_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.ProjectStatQuery)
  })
_sym_db.RegisterMessage(ProjectStatQuery)

_PROJECT = DESCRIPTOR.services_by_name['Project']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROJECT.methods_by_name['create']._options = None
  _PROJECT.methods_by_name['create']._serialized_options = b'\202\323\344\223\002\027\"\025/identity/v1/projects'
  _PROJECT.methods_by_name['update']._options = None
  _PROJECT.methods_by_name['update']._serialized_options = b'\202\323\344\223\002#\032!/identity/v1/project/{project_id}'
  _PROJECT.methods_by_name['delete']._options = None
  _PROJECT.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002#*!/identity/v1/project/{project_id}'
  _PROJECT.methods_by_name['get']._options = None
  _PROJECT.methods_by_name['get']._serialized_options = b'\202\323\344\223\002#\022!/identity/v1/project/{project_id}'
  _PROJECT.methods_by_name['list']._options = None
  _PROJECT.methods_by_name['list']._serialized_options = b'\202\323\344\223\0027\022\025/identity/v1/projectsZ\036\"\034/identity/v1/projects/search'
  _PROJECT.methods_by_name['stat']._options = None
  _PROJECT.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\034\"\032/identity/v1/projects/stat'
  _PROJECT.methods_by_name['add_member']._options = None
  _PROJECT.methods_by_name['add_member']._serialized_options = b'\202\323\344\223\002+\")/identity/v1/project/{project_id}/members'
  _PROJECT.methods_by_name['modify_member']._options = None
  _PROJECT.methods_by_name['modify_member']._serialized_options = b'\202\323\344\223\0024\0322/identity/v1/project/{project_id}/member/{user_id}'
  _PROJECT.methods_by_name['remove_member']._options = None
  _PROJECT.methods_by_name['remove_member']._serialized_options = b'\202\323\344\223\0024*2/identity/v1/project/{project_id}/member/{user_id}'
  _PROJECT.methods_by_name['list_members']._options = None
  _PROJECT.methods_by_name['list_members']._serialized_options = b'\202\323\344\223\002_\022)/identity/v1/project/{project_id}/membersZ2\"0/identity/v1/project/{project_id}/members/search'
  _CREATEPROJECTREQUEST._serialized_start=274
  _CREATEPROJECTREQUEST._serialized_end=394
  _UPDATEPROJECTREQUEST._serialized_start=397
  _UPDATEPROJECTREQUEST._serialized_end=537
  _PROJECTREQUEST._serialized_start=539
  _PROJECTREQUEST._serialized_end=594
  _GETPROJECTREQUEST._serialized_start=596
  _GETPROJECTREQUEST._serialized_end=668
  _PROJECTQUERY._serialized_start=671
  _PROJECTQUERY._serialized_end=825
  _PROJECTINFO._serialized_start=828
  _PROJECTINFO._serialized_end=1045
  _PROJECTSINFO._serialized_start=1047
  _PROJECTSINFO._serialized_end=1138
  _ADDPROJECTMEMBERREQUEST._serialized_start=1141
  _ADDPROJECTMEMBERREQUEST._serialized_end=1348
  _MODIFYPROJECTMEMBERREQUEST._serialized_start=1351
  _MODIFYPROJECTMEMBERREQUEST._serialized_end=1518
  _REMOVEPROJECTMEMBERREQUEST._serialized_start=1520
  _REMOVEPROJECTMEMBERREQUEST._serialized_end=1604
  _PROJECTMEMBERQUERY._serialized_start=1607
  _PROJECTMEMBERQUERY._serialized_end=1775
  _PROJECTROLEBINDINGINFO._serialized_start=1778
  _PROJECTROLEBINDINGINFO._serialized_end=2181
  _PROJECTROLEBINDINGSINFO._serialized_start=2183
  _PROJECTROLEBINDINGSINFO._serialized_end=2296
  _PROJECTSTATQUERY._serialized_start=2298
  _PROJECTSTATQUERY._serialized_end=2389
  _PROJECT._serialized_start=2392
  _PROJECT._serialized_end=3911
# @@protoc_insertion_point(module_scope)
