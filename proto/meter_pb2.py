# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='meter.proto',
  package='energy_meter',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmeter.proto\x12\x0c\x65nergy_meter\x1a\x1fgoogle/protobuf/timestamp.proto\"F\n\x0bMeasurement\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x02 \x01(\x01\"\x8c\x01\n\x0fMeasurementList\x12(\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x04list\x18\x03 \x03(\x0b\x32\x19.energy_meter.Measurementb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_MEASUREMENT = _descriptor.Descriptor(
  name='Measurement',
  full_name='energy_meter.Measurement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='energy_meter.Measurement.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='energy_meter.Measurement.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=62,
  serialized_end=132,
)


_MEASUREMENTLIST = _descriptor.Descriptor(
  name='MeasurementList',
  full_name='energy_meter.MeasurementList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='energy_meter.MeasurementList.from', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='energy_meter.MeasurementList.to', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list', full_name='energy_meter.MeasurementList.list', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=135,
  serialized_end=275,
)

_MEASUREMENT.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MEASUREMENTLIST.fields_by_name['from'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MEASUREMENTLIST.fields_by_name['to'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MEASUREMENTLIST.fields_by_name['list'].message_type = _MEASUREMENT
DESCRIPTOR.message_types_by_name['Measurement'] = _MEASUREMENT
DESCRIPTOR.message_types_by_name['MeasurementList'] = _MEASUREMENTLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Measurement = _reflection.GeneratedProtocolMessageType('Measurement', (_message.Message,), {
  'DESCRIPTOR' : _MEASUREMENT,
  '__module__' : 'meter_pb2'
  # @@protoc_insertion_point(class_scope:energy_meter.Measurement)
  })
_sym_db.RegisterMessage(Measurement)

MeasurementList = _reflection.GeneratedProtocolMessageType('MeasurementList', (_message.Message,), {
  'DESCRIPTOR' : _MEASUREMENTLIST,
  '__module__' : 'meter_pb2'
  # @@protoc_insertion_point(class_scope:energy_meter.MeasurementList)
  })
_sym_db.RegisterMessage(MeasurementList)


# @@protoc_insertion_point(module_scope)