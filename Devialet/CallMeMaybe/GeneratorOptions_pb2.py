# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Devialet/CallMeMaybe/GeneratorOptions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Devialet/CallMeMaybe/GeneratorOptions.proto',
  package='Devialet.CallMeMaybe',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+Devialet/CallMeMaybe/GeneratorOptions.proto\x12\x14\x44\x65vialet.CallMeMaybe\x1a google/protobuf/descriptor.proto\">\n\x14\x45xtendedFieldOptions\x12\x0e\n\x06secret\x18\x01 \x01(\x08\x12\x16\n\x0e\x64isableLogging\x18\x02 \x01(\x08\"\xa2\x02\n\x19\x45xtendedBytesFieldOptions\x12\x42\n\x04type\x18\x01 \x01(\x0e\x32\x34.Devialet.CallMeMaybe.ExtendedBytesFieldOptions.Type\x12H\n\x07logMode\x18\x02 \x01(\x0e\x32\x37.Devialet.CallMeMaybe.ExtendedBytesFieldOptions.LogMode\x12\x14\n\x0clogMaxLength\x18\x03 \x01(\x05\"-\n\x04Type\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x08\n\x04Uuid\x10\x01\x12\x0e\n\nJsonObject\x10\x02\"2\n\x07LogMode\x12\x08\n\x04\x41uto\x10\x00\x12\n\n\x06\x42\x61se64\x10\x01\x12\x07\n\x03Raw\x10\x02\x12\x08\n\x04\x44\x65sc\x10\x03\"\x7f\n\x1a\x45xtendedStringFieldOptions\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x35.Devialet.CallMeMaybe.ExtendedStringFieldOptions.Type\"\x1c\n\x04Type\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x07\n\x03Url\x10\x01\"\xc4\x01\n\x19\x45xtendedInt64FieldOptions\x12\x42\n\x04type\x18\x01 \x01(\x0e\x32\x34.Devialet.CallMeMaybe.ExtendedInt64FieldOptions.Type\"c\n\x04Type\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x0c\n\x08\x44\x61teTime\x10\x01\x12\x0b\n\x07Seconds\x10\x02\x12\x10\n\x0cMilliseconds\x10\x03\x12\x10\n\x0cMicroseconds\x10\x04\x12\x0f\n\x0bNanoseconds\x10\x05\"\x83\x01\n\x1c\x45xtendedRepeatedFieldOptions\x12\x45\n\x04type\x18\x01 \x01(\x0e\x32\x37.Devialet.CallMeMaybe.ExtendedRepeatedFieldOptions.Type\"\x1c\n\x04Type\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x07\n\x03Set\x10\x01\"\xe0\x01\n\x17\x45xtendedMapFieldOptions\x12@\n\x04type\x18\x01 \x01(\x0e\x32\x32.Devialet.CallMeMaybe.ExtendedMapFieldOptions.Type\x12\x46\n\x07keyType\x18\x02 \x01(\x0e\x32\x35.Devialet.CallMeMaybe.ExtendedMapFieldOptions.KeyType\"\x19\n\x04Type\x12\x07\n\x03Map\x10\x00\x12\x08\n\x04Hash\x10\x01\" \n\x07KeyType\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x08\n\x04Uuid\x10\x01\"\xc7\x01\n\x1c\x45xtendedPropertyFieldOptions\x12\x19\n\x11minimumApiVersion\x18\x01 \x01(\r\x12\x19\n\x11maximumApiVersion\x18\x02 \x01(\r\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x12\x10\n\x08\x63onstant\x18\x04 \x01(\x08\x12\x16\n\x0e\x64isableLogging\x18\x05 \x01(\x08\x12\x1c\n\x14\x64isableUpdateLogging\x18\x06 \x01(\x08\x12\x17\n\x0fsupportsReplace\x18\x07 \x01(\x08\"^\n\x16\x45xtendedServiceOptions\x12\x12\n\napiVersion\x18\x01 \x01(\r\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\nproperties\x18\x04 \x01(\t\"\x99\x01\n\x15\x45xtendedMethodOptions\x12\x19\n\x11minimumApiVersion\x18\x01 \x01(\r\x12\x19\n\x11maximumApiVersion\x18\x02 \x01(\r\x12\x14\n\x0cnotification\x18\x03 \x01(\x08\x12\x16\n\x0e\x64isableLogging\x18\x04 \x01(\x08\x12\x1c\n\x14useMessageAsArgument\x18\x05 \x01(\x08\"/\n\x18\x45xtendedEnumValueOptions\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t:e\n\tenumValue\x12!.google.protobuf.EnumValueOptions\x18\xe8\x07 \x01(\x0b\x32..Devialet.CallMeMaybe.ExtendedEnumValueOptions:Y\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\xe8\x07 \x01(\x0b\x32*.Devialet.CallMeMaybe.ExtendedFieldOptions:^\n\x05\x62ytes\x12\x1d.google.protobuf.FieldOptions\x18\xe9\x07 \x01(\x0b\x32/.Devialet.CallMeMaybe.ExtendedBytesFieldOptions:Z\n\x03map\x12\x1d.google.protobuf.FieldOptions\x18\xea\x07 \x01(\x0b\x32-.Devialet.CallMeMaybe.ExtendedMapFieldOptions:d\n\x08property\x12\x1d.google.protobuf.FieldOptions\x18\xeb\x07 \x01(\x0b\x32\x32.Devialet.CallMeMaybe.ExtendedPropertyFieldOptions:`\n\x06string\x12\x1d.google.protobuf.FieldOptions\x18\xec\x07 \x01(\x0b\x32\x30.Devialet.CallMeMaybe.ExtendedStringFieldOptions:^\n\x05int64\x12\x1d.google.protobuf.FieldOptions\x18\xed\x07 \x01(\x0b\x32/.Devialet.CallMeMaybe.ExtendedInt64FieldOptions:d\n\x08repeated\x12\x1d.google.protobuf.FieldOptions\x18\xee\x07 \x01(\x0b\x32\x32.Devialet.CallMeMaybe.ExtendedRepeatedFieldOptions:_\n\x07service\x12\x1f.google.protobuf.ServiceOptions\x18\xe8\x07 \x01(\x0b\x32,.Devialet.CallMeMaybe.ExtendedServiceOptions:\\\n\x06method\x12\x1e.google.protobuf.MethodOptions\x18\xe8\x07 \x01(\x0b\x32+.Devialet.CallMeMaybe.ExtendedMethodOptionsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


ENUMVALUE_FIELD_NUMBER = 1000
enumValue = _descriptor.FieldDescriptor(
  name='enumValue', full_name='Devialet.CallMeMaybe.enumValue', index=0,
  number=1000, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
FIELD_FIELD_NUMBER = 1000
field = _descriptor.FieldDescriptor(
  name='field', full_name='Devialet.CallMeMaybe.field', index=1,
  number=1000, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
BYTES_FIELD_NUMBER = 1001
bytes = _descriptor.FieldDescriptor(
  name='bytes', full_name='Devialet.CallMeMaybe.bytes', index=2,
  number=1001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
MAP_FIELD_NUMBER = 1002
map = _descriptor.FieldDescriptor(
  name='map', full_name='Devialet.CallMeMaybe.map', index=3,
  number=1002, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
PROPERTY_FIELD_NUMBER = 1003
property = _descriptor.FieldDescriptor(
  name='property', full_name='Devialet.CallMeMaybe.property', index=4,
  number=1003, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
STRING_FIELD_NUMBER = 1004
string = _descriptor.FieldDescriptor(
  name='string', full_name='Devialet.CallMeMaybe.string', index=5,
  number=1004, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
INT64_FIELD_NUMBER = 1005
int64 = _descriptor.FieldDescriptor(
  name='int64', full_name='Devialet.CallMeMaybe.int64', index=6,
  number=1005, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
REPEATED_FIELD_NUMBER = 1006
repeated = _descriptor.FieldDescriptor(
  name='repeated', full_name='Devialet.CallMeMaybe.repeated', index=7,
  number=1006, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
SERVICE_FIELD_NUMBER = 1000
service = _descriptor.FieldDescriptor(
  name='service', full_name='Devialet.CallMeMaybe.service', index=8,
  number=1000, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
METHOD_FIELD_NUMBER = 1000
method = _descriptor.FieldDescriptor(
  name='method', full_name='Devialet.CallMeMaybe.method', index=9,
  number=1000, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

_EXTENDEDBYTESFIELDOPTIONS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Devialet.CallMeMaybe.ExtendedBytesFieldOptions.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Uuid', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JsonObject', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=361,
  serialized_end=406,
)
_sym_db.RegisterEnumDescriptor(_EXTENDEDBYTESFIELDOPTIONS_TYPE)

_EXTENDEDBYTESFIELDOPTIONS_LOGMODE = _descriptor.EnumDescriptor(
  name='LogMode',
  full_name='Devialet.CallMeMaybe.ExtendedBytesFieldOptions.LogMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Auto', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Base64', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Raw', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Desc', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=408,
  serialized_end=458,
)
_sym_db.RegisterEnumDescriptor(_EXTENDEDBYTESFIELDOPTIONS_LOGMODE)

_EXTENDEDSTRINGFIELDOPTIONS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Devialet.CallMeMaybe.ExtendedStringFieldOptions.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Url', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=559,
  serialized_end=587,
)
_sym_db.RegisterEnumDescriptor(_EXTENDEDSTRINGFIELDOPTIONS_TYPE)

_EXTENDEDINT64FIELDOPTIONS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Devialet.CallMeMaybe.ExtendedInt64FieldOptions.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DateTime', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Seconds', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Milliseconds', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Microseconds', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Nanoseconds', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=687,
  serialized_end=786,
)
_sym_db.RegisterEnumDescriptor(_EXTENDEDINT64FIELDOPTIONS_TYPE)

_EXTENDEDREPEATEDFIELDOPTIONS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Devialet.CallMeMaybe.ExtendedRepeatedFieldOptions.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Set', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=892,
  serialized_end=920,
)
_sym_db.RegisterEnumDescriptor(_EXTENDEDREPEATEDFIELDOPTIONS_TYPE)

_EXTENDEDMAPFIELDOPTIONS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Devialet.CallMeMaybe.ExtendedMapFieldOptions.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Map', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Hash', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1088,
  serialized_end=1113,
)
_sym_db.RegisterEnumDescriptor(_EXTENDEDMAPFIELDOPTIONS_TYPE)

_EXTENDEDMAPFIELDOPTIONS_KEYTYPE = _descriptor.EnumDescriptor(
  name='KeyType',
  full_name='Devialet.CallMeMaybe.ExtendedMapFieldOptions.KeyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Uuid', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1115,
  serialized_end=1147,
)
_sym_db.RegisterEnumDescriptor(_EXTENDEDMAPFIELDOPTIONS_KEYTYPE)


_EXTENDEDFIELDOPTIONS = _descriptor.Descriptor(
  name='ExtendedFieldOptions',
  full_name='Devialet.CallMeMaybe.ExtendedFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret', full_name='Devialet.CallMeMaybe.ExtendedFieldOptions.secret', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disableLogging', full_name='Devialet.CallMeMaybe.ExtendedFieldOptions.disableLogging', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=103,
  serialized_end=165,
)


_EXTENDEDBYTESFIELDOPTIONS = _descriptor.Descriptor(
  name='ExtendedBytesFieldOptions',
  full_name='Devialet.CallMeMaybe.ExtendedBytesFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Devialet.CallMeMaybe.ExtendedBytesFieldOptions.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logMode', full_name='Devialet.CallMeMaybe.ExtendedBytesFieldOptions.logMode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logMaxLength', full_name='Devialet.CallMeMaybe.ExtendedBytesFieldOptions.logMaxLength', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTENDEDBYTESFIELDOPTIONS_TYPE,
    _EXTENDEDBYTESFIELDOPTIONS_LOGMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=458,
)


_EXTENDEDSTRINGFIELDOPTIONS = _descriptor.Descriptor(
  name='ExtendedStringFieldOptions',
  full_name='Devialet.CallMeMaybe.ExtendedStringFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Devialet.CallMeMaybe.ExtendedStringFieldOptions.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTENDEDSTRINGFIELDOPTIONS_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=587,
)


_EXTENDEDINT64FIELDOPTIONS = _descriptor.Descriptor(
  name='ExtendedInt64FieldOptions',
  full_name='Devialet.CallMeMaybe.ExtendedInt64FieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Devialet.CallMeMaybe.ExtendedInt64FieldOptions.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTENDEDINT64FIELDOPTIONS_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=786,
)


_EXTENDEDREPEATEDFIELDOPTIONS = _descriptor.Descriptor(
  name='ExtendedRepeatedFieldOptions',
  full_name='Devialet.CallMeMaybe.ExtendedRepeatedFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Devialet.CallMeMaybe.ExtendedRepeatedFieldOptions.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTENDEDREPEATEDFIELDOPTIONS_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=789,
  serialized_end=920,
)


_EXTENDEDMAPFIELDOPTIONS = _descriptor.Descriptor(
  name='ExtendedMapFieldOptions',
  full_name='Devialet.CallMeMaybe.ExtendedMapFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Devialet.CallMeMaybe.ExtendedMapFieldOptions.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyType', full_name='Devialet.CallMeMaybe.ExtendedMapFieldOptions.keyType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTENDEDMAPFIELDOPTIONS_TYPE,
    _EXTENDEDMAPFIELDOPTIONS_KEYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=923,
  serialized_end=1147,
)


_EXTENDEDPROPERTYFIELDOPTIONS = _descriptor.Descriptor(
  name='ExtendedPropertyFieldOptions',
  full_name='Devialet.CallMeMaybe.ExtendedPropertyFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimumApiVersion', full_name='Devialet.CallMeMaybe.ExtendedPropertyFieldOptions.minimumApiVersion', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximumApiVersion', full_name='Devialet.CallMeMaybe.ExtendedPropertyFieldOptions.maximumApiVersion', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='Devialet.CallMeMaybe.ExtendedPropertyFieldOptions.readOnly', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constant', full_name='Devialet.CallMeMaybe.ExtendedPropertyFieldOptions.constant', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disableLogging', full_name='Devialet.CallMeMaybe.ExtendedPropertyFieldOptions.disableLogging', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disableUpdateLogging', full_name='Devialet.CallMeMaybe.ExtendedPropertyFieldOptions.disableUpdateLogging', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportsReplace', full_name='Devialet.CallMeMaybe.ExtendedPropertyFieldOptions.supportsReplace', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1150,
  serialized_end=1349,
)


_EXTENDEDSERVICEOPTIONS = _descriptor.Descriptor(
  name='ExtendedServiceOptions',
  full_name='Devialet.CallMeMaybe.ExtendedServiceOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apiVersion', full_name='Devialet.CallMeMaybe.ExtendedServiceOptions.apiVersion', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='Devialet.CallMeMaybe.ExtendedServiceOptions.parent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Devialet.CallMeMaybe.ExtendedServiceOptions.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='Devialet.CallMeMaybe.ExtendedServiceOptions.properties', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1351,
  serialized_end=1445,
)


_EXTENDEDMETHODOPTIONS = _descriptor.Descriptor(
  name='ExtendedMethodOptions',
  full_name='Devialet.CallMeMaybe.ExtendedMethodOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimumApiVersion', full_name='Devialet.CallMeMaybe.ExtendedMethodOptions.minimumApiVersion', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximumApiVersion', full_name='Devialet.CallMeMaybe.ExtendedMethodOptions.maximumApiVersion', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notification', full_name='Devialet.CallMeMaybe.ExtendedMethodOptions.notification', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disableLogging', full_name='Devialet.CallMeMaybe.ExtendedMethodOptions.disableLogging', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='useMessageAsArgument', full_name='Devialet.CallMeMaybe.ExtendedMethodOptions.useMessageAsArgument', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1448,
  serialized_end=1601,
)


_EXTENDEDENUMVALUEOPTIONS = _descriptor.Descriptor(
  name='ExtendedEnumValueOptions',
  full_name='Devialet.CallMeMaybe.ExtendedEnumValueOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='Devialet.CallMeMaybe.ExtendedEnumValueOptions.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1603,
  serialized_end=1650,
)

_EXTENDEDBYTESFIELDOPTIONS.fields_by_name['type'].enum_type = _EXTENDEDBYTESFIELDOPTIONS_TYPE
_EXTENDEDBYTESFIELDOPTIONS.fields_by_name['logMode'].enum_type = _EXTENDEDBYTESFIELDOPTIONS_LOGMODE
_EXTENDEDBYTESFIELDOPTIONS_TYPE.containing_type = _EXTENDEDBYTESFIELDOPTIONS
_EXTENDEDBYTESFIELDOPTIONS_LOGMODE.containing_type = _EXTENDEDBYTESFIELDOPTIONS
_EXTENDEDSTRINGFIELDOPTIONS.fields_by_name['type'].enum_type = _EXTENDEDSTRINGFIELDOPTIONS_TYPE
_EXTENDEDSTRINGFIELDOPTIONS_TYPE.containing_type = _EXTENDEDSTRINGFIELDOPTIONS
_EXTENDEDINT64FIELDOPTIONS.fields_by_name['type'].enum_type = _EXTENDEDINT64FIELDOPTIONS_TYPE
_EXTENDEDINT64FIELDOPTIONS_TYPE.containing_type = _EXTENDEDINT64FIELDOPTIONS
_EXTENDEDREPEATEDFIELDOPTIONS.fields_by_name['type'].enum_type = _EXTENDEDREPEATEDFIELDOPTIONS_TYPE
_EXTENDEDREPEATEDFIELDOPTIONS_TYPE.containing_type = _EXTENDEDREPEATEDFIELDOPTIONS
_EXTENDEDMAPFIELDOPTIONS.fields_by_name['type'].enum_type = _EXTENDEDMAPFIELDOPTIONS_TYPE
_EXTENDEDMAPFIELDOPTIONS.fields_by_name['keyType'].enum_type = _EXTENDEDMAPFIELDOPTIONS_KEYTYPE
_EXTENDEDMAPFIELDOPTIONS_TYPE.containing_type = _EXTENDEDMAPFIELDOPTIONS
_EXTENDEDMAPFIELDOPTIONS_KEYTYPE.containing_type = _EXTENDEDMAPFIELDOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedFieldOptions'] = _EXTENDEDFIELDOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedBytesFieldOptions'] = _EXTENDEDBYTESFIELDOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedStringFieldOptions'] = _EXTENDEDSTRINGFIELDOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedInt64FieldOptions'] = _EXTENDEDINT64FIELDOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedRepeatedFieldOptions'] = _EXTENDEDREPEATEDFIELDOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedMapFieldOptions'] = _EXTENDEDMAPFIELDOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedPropertyFieldOptions'] = _EXTENDEDPROPERTYFIELDOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedServiceOptions'] = _EXTENDEDSERVICEOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedMethodOptions'] = _EXTENDEDMETHODOPTIONS
DESCRIPTOR.message_types_by_name['ExtendedEnumValueOptions'] = _EXTENDEDENUMVALUEOPTIONS
DESCRIPTOR.extensions_by_name['enumValue'] = enumValue
DESCRIPTOR.extensions_by_name['field'] = field
DESCRIPTOR.extensions_by_name['bytes'] = bytes
DESCRIPTOR.extensions_by_name['map'] = map
DESCRIPTOR.extensions_by_name['property'] = property
DESCRIPTOR.extensions_by_name['string'] = string
DESCRIPTOR.extensions_by_name['int64'] = int64
DESCRIPTOR.extensions_by_name['repeated'] = repeated
DESCRIPTOR.extensions_by_name['service'] = service
DESCRIPTOR.extensions_by_name['method'] = method
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtendedFieldOptions = _reflection.GeneratedProtocolMessageType('ExtendedFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDFIELDOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedFieldOptions)
  ))
_sym_db.RegisterMessage(ExtendedFieldOptions)

ExtendedBytesFieldOptions = _reflection.GeneratedProtocolMessageType('ExtendedBytesFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDBYTESFIELDOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedBytesFieldOptions)
  ))
_sym_db.RegisterMessage(ExtendedBytesFieldOptions)

ExtendedStringFieldOptions = _reflection.GeneratedProtocolMessageType('ExtendedStringFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDSTRINGFIELDOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedStringFieldOptions)
  ))
_sym_db.RegisterMessage(ExtendedStringFieldOptions)

ExtendedInt64FieldOptions = _reflection.GeneratedProtocolMessageType('ExtendedInt64FieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDINT64FIELDOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedInt64FieldOptions)
  ))
_sym_db.RegisterMessage(ExtendedInt64FieldOptions)

ExtendedRepeatedFieldOptions = _reflection.GeneratedProtocolMessageType('ExtendedRepeatedFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDREPEATEDFIELDOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedRepeatedFieldOptions)
  ))
_sym_db.RegisterMessage(ExtendedRepeatedFieldOptions)

ExtendedMapFieldOptions = _reflection.GeneratedProtocolMessageType('ExtendedMapFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDMAPFIELDOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedMapFieldOptions)
  ))
_sym_db.RegisterMessage(ExtendedMapFieldOptions)

ExtendedPropertyFieldOptions = _reflection.GeneratedProtocolMessageType('ExtendedPropertyFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDPROPERTYFIELDOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedPropertyFieldOptions)
  ))
_sym_db.RegisterMessage(ExtendedPropertyFieldOptions)

ExtendedServiceOptions = _reflection.GeneratedProtocolMessageType('ExtendedServiceOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDSERVICEOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedServiceOptions)
  ))
_sym_db.RegisterMessage(ExtendedServiceOptions)

ExtendedMethodOptions = _reflection.GeneratedProtocolMessageType('ExtendedMethodOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDMETHODOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedMethodOptions)
  ))
_sym_db.RegisterMessage(ExtendedMethodOptions)

ExtendedEnumValueOptions = _reflection.GeneratedProtocolMessageType('ExtendedEnumValueOptions', (_message.Message,), dict(
  DESCRIPTOR = _EXTENDEDENUMVALUEOPTIONS,
  __module__ = 'Devialet.CallMeMaybe.GeneratorOptions_pb2'
  # @@protoc_insertion_point(class_scope:Devialet.CallMeMaybe.ExtendedEnumValueOptions)
  ))
_sym_db.RegisterMessage(ExtendedEnumValueOptions)

enumValue.message_type = _EXTENDEDENUMVALUEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enumValue)
field.message_type = _EXTENDEDFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field)
bytes.message_type = _EXTENDEDBYTESFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(bytes)
map.message_type = _EXTENDEDMAPFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(map)
property.message_type = _EXTENDEDPROPERTYFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(property)
string.message_type = _EXTENDEDSTRINGFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(string)
int64.message_type = _EXTENDEDINT64FIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(int64)
repeated.message_type = _EXTENDEDREPEATEDFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(repeated)
service.message_type = _EXTENDEDSERVICEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service)
method.message_type = _EXTENDEDMETHODOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(method)

# @@protoc_insertion_point(module_scope)
