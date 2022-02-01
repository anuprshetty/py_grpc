# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rest_grpc_dual_mode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rest_grpc_dual_mode.proto',
  package='rest_grpc_dual_mode',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19rest_grpc_dual_mode.proto\x12\x13rest_grpc_dual_mode\"I\n\x0eRequestMessage\x12\x14\n\x0c\x64\x61taCommType\x18\x01 \x01(\t\x12\x13\n\x0bmessageType\x18\x02 \x01(\t\x12\x0c\n\x04year\x18\x03 \x01(\x05\"=\n\x0fResponseMessage\x12\x11\n\tgreetings\x18\x01 \x01(\t\x12\x17\n\x0fmessageReceived\x18\x02 \x01(\x08\x32u\n\x12GreetingsGenerator\x12_\n\x10GRPCGetGreetings\x12#.rest_grpc_dual_mode.RequestMessage\x1a$.rest_grpc_dual_mode.ResponseMessage\"\x00\x62\x06proto3'
)




_REQUESTMESSAGE = _descriptor.Descriptor(
  name='RequestMessage',
  full_name='rest_grpc_dual_mode.RequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataCommType', full_name='rest_grpc_dual_mode.RequestMessage.dataCommType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messageType', full_name='rest_grpc_dual_mode.RequestMessage.messageType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='rest_grpc_dual_mode.RequestMessage.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=123,
)


_RESPONSEMESSAGE = _descriptor.Descriptor(
  name='ResponseMessage',
  full_name='rest_grpc_dual_mode.ResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='greetings', full_name='rest_grpc_dual_mode.ResponseMessage.greetings', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messageReceived', full_name='rest_grpc_dual_mode.ResponseMessage.messageReceived', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=186,
)

DESCRIPTOR.message_types_by_name['RequestMessage'] = _REQUESTMESSAGE
DESCRIPTOR.message_types_by_name['ResponseMessage'] = _RESPONSEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestMessage = _reflection.GeneratedProtocolMessageType('RequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMESSAGE,
  '__module__' : 'rest_grpc_dual_mode_pb2'
  # @@protoc_insertion_point(class_scope:rest_grpc_dual_mode.RequestMessage)
  })
_sym_db.RegisterMessage(RequestMessage)

ResponseMessage = _reflection.GeneratedProtocolMessageType('ResponseMessage', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEMESSAGE,
  '__module__' : 'rest_grpc_dual_mode_pb2'
  # @@protoc_insertion_point(class_scope:rest_grpc_dual_mode.ResponseMessage)
  })
_sym_db.RegisterMessage(ResponseMessage)



_GREETINGSGENERATOR = _descriptor.ServiceDescriptor(
  name='GreetingsGenerator',
  full_name='rest_grpc_dual_mode.GreetingsGenerator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=188,
  serialized_end=305,
  methods=[
  _descriptor.MethodDescriptor(
    name='GRPCGetGreetings',
    full_name='rest_grpc_dual_mode.GreetingsGenerator.GRPCGetGreetings',
    index=0,
    containing_service=None,
    input_type=_REQUESTMESSAGE,
    output_type=_RESPONSEMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETINGSGENERATOR)

DESCRIPTOR.services_by_name['GreetingsGenerator'] = _GREETINGSGENERATOR

# @@protoc_insertion_point(module_scope)