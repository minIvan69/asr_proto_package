# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: my_asr_proto/asr.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'my_asr_proto/asr.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16my_asr_proto/asr.proto\x12\x03\x61sr\":\n\x11TranscribeRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x13\n\x0b\x66older_path\x18\x02 \x01(\t\"\"\n\x12TranscribeResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\"3\n\x10RecognizeRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x11\n\tthreshold\x18\x02 \x01(\x01\"P\n\x11RecognizeResponse\x12\x12\n\nrecognized\x18\x01 \x01(\x08\x12\x12\n\nfirst_part\x18\x02 \x01(\t\x12\x13\n\x0bsecond_part\x18\x03 \x01(\t2\x87\x01\n\nASRService\x12=\n\nTranscribe\x12\x16.asr.TranscribeRequest\x1a\x17.asr.TranscribeResponse\x12:\n\tRecognize\x12\x15.asr.RecognizeRequest\x1a\x16.asr.RecognizeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_asr_proto.asr_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRANSCRIBEREQUEST']._serialized_start=31
  _globals['_TRANSCRIBEREQUEST']._serialized_end=89
  _globals['_TRANSCRIBERESPONSE']._serialized_start=91
  _globals['_TRANSCRIBERESPONSE']._serialized_end=125
  _globals['_RECOGNIZEREQUEST']._serialized_start=127
  _globals['_RECOGNIZEREQUEST']._serialized_end=178
  _globals['_RECOGNIZERESPONSE']._serialized_start=180
  _globals['_RECOGNIZERESPONSE']._serialized_end=260
  _globals['_ASRSERVICE']._serialized_start=263
  _globals['_ASRSERVICE']._serialized_end=398
# @@protoc_insertion_point(module_scope)
