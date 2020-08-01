# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/vision_v1p4beta1/proto/face.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.vision_v1p4beta1.proto import geometry_pb2 as google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/vision_v1p4beta1/proto/face.proto',
  package='google.cloud.vision.v1p4beta1',
  syntax='proto3',
  serialized_options=b'\n!com.google.cloud.vision.v1p4beta1B\016CelebrityProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p4beta1;vision\370\001\001\242\002\004GCVN',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.google/cloud/vision_v1p4beta1/proto/face.proto\x12\x1dgoogle.cloud.vision.v1p4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x32google/cloud/vision_v1p4beta1/proto/geometry.proto\".\n\x15\x46\x61\x63\x65RecognitionParams\x12\x15\n\rcelebrity_set\x18\x01 \x03(\t\"D\n\tCelebrity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"h\n\x15\x46\x61\x63\x65RecognitionResult\x12;\n\tcelebrity\x18\x01 \x01(\x0b\x32(.google.cloud.vision.v1p4beta1.Celebrity\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x42\x84\x01\n!com.google.cloud.vision.v1p4beta1B\x0e\x43\x65lebrityProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p4beta1;vision\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_geometry__pb2.DESCRIPTOR,])




_FACERECOGNITIONPARAMS = _descriptor.Descriptor(
  name='FaceRecognitionParams',
  full_name='google.cloud.vision.v1p4beta1.FaceRecognitionParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='celebrity_set', full_name='google.cloud.vision.v1p4beta1.FaceRecognitionParams.celebrity_set', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=163,
  serialized_end=209,
)


_CELEBRITY = _descriptor.Descriptor(
  name='Celebrity',
  full_name='google.cloud.vision.v1p4beta1.Celebrity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.vision.v1p4beta1.Celebrity.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.vision.v1p4beta1.Celebrity.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.vision.v1p4beta1.Celebrity.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=211,
  serialized_end=279,
)


_FACERECOGNITIONRESULT = _descriptor.Descriptor(
  name='FaceRecognitionResult',
  full_name='google.cloud.vision.v1p4beta1.FaceRecognitionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='celebrity', full_name='google.cloud.vision.v1p4beta1.FaceRecognitionResult.celebrity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='google.cloud.vision.v1p4beta1.FaceRecognitionResult.confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=281,
  serialized_end=385,
)

_FACERECOGNITIONRESULT.fields_by_name['celebrity'].message_type = _CELEBRITY
DESCRIPTOR.message_types_by_name['FaceRecognitionParams'] = _FACERECOGNITIONPARAMS
DESCRIPTOR.message_types_by_name['Celebrity'] = _CELEBRITY
DESCRIPTOR.message_types_by_name['FaceRecognitionResult'] = _FACERECOGNITIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaceRecognitionParams = _reflection.GeneratedProtocolMessageType('FaceRecognitionParams', (_message.Message,), {
  'DESCRIPTOR' : _FACERECOGNITIONPARAMS,
  '__module__' : 'google.cloud.vision_v1p4beta1.proto.face_pb2'
  ,
  '__doc__': """Parameters for a celebrity recognition request.
  
  Attributes:
      celebrity_set:
          The resource names for one or more
          [CelebritySet][google.cloud.vision.v1p4beta1.CelebritySet]s. A
          celebrity set is preloaded and can be specified as
          “builtin/default”. If this is specified, the algorithm will
          try to match the faces detected in the input image to the
          Celebrities in the CelebritySets.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p4beta1.FaceRecognitionParams)
  })
_sym_db.RegisterMessage(FaceRecognitionParams)

Celebrity = _reflection.GeneratedProtocolMessageType('Celebrity', (_message.Message,), {
  'DESCRIPTOR' : _CELEBRITY,
  '__module__' : 'google.cloud.vision_v1p4beta1.proto.face_pb2'
  ,
  '__doc__': """A Celebrity is a group of Faces with an identity.
  
  Attributes:
      name:
          The resource name of the preloaded Celebrity. Has the format
          ``builtin/{mid}``.
      display_name:
          The Celebrity’s display name.
      description:
          The Celebrity’s description.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p4beta1.Celebrity)
  })
_sym_db.RegisterMessage(Celebrity)

FaceRecognitionResult = _reflection.GeneratedProtocolMessageType('FaceRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _FACERECOGNITIONRESULT,
  '__module__' : 'google.cloud.vision_v1p4beta1.proto.face_pb2'
  ,
  '__doc__': """Information about a face’s identity.
  
  Attributes:
      celebrity:
          The [Celebrity][google.cloud.vision.v1p4beta1.Celebrity] that
          this face was matched to.
      confidence:
          Recognition confidence. Range [0, 1].
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p4beta1.FaceRecognitionResult)
  })
_sym_db.RegisterMessage(FaceRecognitionResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
