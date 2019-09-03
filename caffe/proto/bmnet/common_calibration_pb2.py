# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bmnet/common_calibration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bmnet/common_calibration.proto',
  package='',
  serialized_pb=_b('\n\x1e\x62mnet/common_calibration.proto\"\xcb\x01\n*ConvolutionCalibrationCalibrationParameter\x12\x1c\n\x14\x62n_right_shift_width\x18\x01 \x01(\x05\x12\x1f\n\x17scale_right_shift_width\x18\x02 \x01(\x05\x12/\n\x0bprelu_param\x18\x03 \x01(\x0b\x32\x1a.PReLUCalibrationParameter\x12-\n\nrelu_param\x18\x04 \x01(\x0b\x32\x19.ReLUCalibrationParameter\"S\n InnerProductCalibrationParameter\x12/\n\x0bprelu_param\x18\x03 \x01(\x0b\x32\x1a.PReLUCalibrationParameter\"\x1d\n\x1bPoolingCalibrationParameter\"z\n\x18ReLUCalibrationParameter\x12\x10\n\x08gt_scale\x18\x01 \x02(\x05\x12\x10\n\x08le_scale\x18\x02 \x02(\x05\x12\x1c\n\x14gt_right_shift_width\x18\x03 \x02(\x05\x12\x1c\n\x14le_right_shift_width\x18\x04 \x02(\x05\"i\n\x19PReLUCalibrationParameter\x12\x10\n\x08gt_scale\x18\x01 \x02(\x05\x12\x1c\n\x14gt_right_shift_width\x18\x02 \x02(\x05\x12\x1c\n\x14le_right_shift_width\x18\x03 \x02(\x05\"t\n\x1a\x43oncatCalibrationParameter\x12\x19\n\x11right_shift_width\x18\x01 \x03(\x05\x12\x1d\n\x15threshold_x_quantized\x18\x02 \x03(\x05\x12\x1c\n\x11need_quantize_num\x18\x03 \x02(\x05:\x01\x30\"\x7f\n\x1dLeakyReLUCalibrationParameter\x12\x10\n\x08gt_scale\x18\x01 \x02(\x05\x12\x10\n\x08le_scale\x18\x02 \x02(\x05\x12\x1c\n\x14gt_right_shift_width\x18\x03 \x02(\x05\x12\x1c\n\x14le_right_shift_width\x18\x04 \x02(\x05\"\xec\x04\n\x19LayerCalibrationParameter\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0bthreshold_y\x18\x02 \x03(\x02\x12\x19\n\x11right_shift_width\x18\x03 \x01(\x05\x12\x1d\n\x15threshold_x_quantized\x18\x04 \x03(\x05\x12\"\n\nblob_param\x18\x05 \x03(\x0b\x32\x0e.BlobParameter\x12\x16\n\x0e\x66usion_skipped\x18\x06 \x01(\x05\x12\x17\n\x0f\x62ottom_unsigned\x18\x07 \x03(\x08\x12\x14\n\x0ctop_unsigned\x18\x08 \x03(\x08\x12\x46\n\x11\x63onvolution_param\x18j \x01(\x0b\x32+.ConvolutionCalibrationCalibrationParameter\x12>\n\x13inner_product_param\x18u \x01(\x0b\x32!.InnerProductCalibrationParameter\x12\x33\n\rpooling_param\x18y \x01(\x0b\x32\x1c.PoolingCalibrationParameter\x12-\n\nrelu_param\x18{ \x01(\x0b\x32\x19.ReLUCalibrationParameter\x12/\n\x0bprelu_param\x18| \x01(\x0b\x32\x1a.PReLUCalibrationParameter\x12\x31\n\x0c\x63oncat_param\x18} \x01(\x0b\x32\x1b.ConcatCalibrationParameter\x12\x37\n\x0fleakyrelu_param\x18~ \x01(\x0b\x32\x1e.LeakyReLUCalibrationParameter\"M\n\rBlobParameter\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0bthreshold_y\x18\x02 \x02(\x02\x12\x19\n\x11right_shift_width\x18\x03 \x01(\x05\"R\n\x17NetCalibrationParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x05layer\x18\x64 \x03(\x0b\x32\x1a.LayerCalibrationParameter')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONVOLUTIONCALIBRATIONCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='ConvolutionCalibrationCalibrationParameter',
  full_name='ConvolutionCalibrationCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bn_right_shift_width', full_name='ConvolutionCalibrationCalibrationParameter.bn_right_shift_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale_right_shift_width', full_name='ConvolutionCalibrationCalibrationParameter.scale_right_shift_width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prelu_param', full_name='ConvolutionCalibrationCalibrationParameter.prelu_param', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relu_param', full_name='ConvolutionCalibrationCalibrationParameter.relu_param', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=238,
)


_INNERPRODUCTCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='InnerProductCalibrationParameter',
  full_name='InnerProductCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prelu_param', full_name='InnerProductCalibrationParameter.prelu_param', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=323,
)


_POOLINGCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='PoolingCalibrationParameter',
  full_name='PoolingCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=354,
)


_RELUCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='ReLUCalibrationParameter',
  full_name='ReLUCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gt_scale', full_name='ReLUCalibrationParameter.gt_scale', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='le_scale', full_name='ReLUCalibrationParameter.le_scale', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gt_right_shift_width', full_name='ReLUCalibrationParameter.gt_right_shift_width', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='le_right_shift_width', full_name='ReLUCalibrationParameter.le_right_shift_width', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=478,
)


_PRELUCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='PReLUCalibrationParameter',
  full_name='PReLUCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gt_scale', full_name='PReLUCalibrationParameter.gt_scale', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gt_right_shift_width', full_name='PReLUCalibrationParameter.gt_right_shift_width', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='le_right_shift_width', full_name='PReLUCalibrationParameter.le_right_shift_width', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=585,
)


_CONCATCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='ConcatCalibrationParameter',
  full_name='ConcatCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='right_shift_width', full_name='ConcatCalibrationParameter.right_shift_width', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threshold_x_quantized', full_name='ConcatCalibrationParameter.threshold_x_quantized', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='need_quantize_num', full_name='ConcatCalibrationParameter.need_quantize_num', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=587,
  serialized_end=703,
)


_LEAKYRELUCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='LeakyReLUCalibrationParameter',
  full_name='LeakyReLUCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gt_scale', full_name='LeakyReLUCalibrationParameter.gt_scale', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='le_scale', full_name='LeakyReLUCalibrationParameter.le_scale', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gt_right_shift_width', full_name='LeakyReLUCalibrationParameter.gt_right_shift_width', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='le_right_shift_width', full_name='LeakyReLUCalibrationParameter.le_right_shift_width', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=705,
  serialized_end=832,
)


_LAYERCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='LayerCalibrationParameter',
  full_name='LayerCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='LayerCalibrationParameter.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threshold_y', full_name='LayerCalibrationParameter.threshold_y', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_shift_width', full_name='LayerCalibrationParameter.right_shift_width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threshold_x_quantized', full_name='LayerCalibrationParameter.threshold_x_quantized', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blob_param', full_name='LayerCalibrationParameter.blob_param', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fusion_skipped', full_name='LayerCalibrationParameter.fusion_skipped', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bottom_unsigned', full_name='LayerCalibrationParameter.bottom_unsigned', index=6,
      number=7, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top_unsigned', full_name='LayerCalibrationParameter.top_unsigned', index=7,
      number=8, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='convolution_param', full_name='LayerCalibrationParameter.convolution_param', index=8,
      number=106, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inner_product_param', full_name='LayerCalibrationParameter.inner_product_param', index=9,
      number=117, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pooling_param', full_name='LayerCalibrationParameter.pooling_param', index=10,
      number=121, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relu_param', full_name='LayerCalibrationParameter.relu_param', index=11,
      number=123, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prelu_param', full_name='LayerCalibrationParameter.prelu_param', index=12,
      number=124, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='concat_param', full_name='LayerCalibrationParameter.concat_param', index=13,
      number=125, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leakyrelu_param', full_name='LayerCalibrationParameter.leakyrelu_param', index=14,
      number=126, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=835,
  serialized_end=1455,
)


_BLOBPARAMETER = _descriptor.Descriptor(
  name='BlobParameter',
  full_name='BlobParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='BlobParameter.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threshold_y', full_name='BlobParameter.threshold_y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_shift_width', full_name='BlobParameter.right_shift_width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1457,
  serialized_end=1534,
)


_NETCALIBRATIONPARAMETER = _descriptor.Descriptor(
  name='NetCalibrationParameter',
  full_name='NetCalibrationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='NetCalibrationParameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layer', full_name='NetCalibrationParameter.layer', index=1,
      number=100, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1536,
  serialized_end=1618,
)

_CONVOLUTIONCALIBRATIONCALIBRATIONPARAMETER.fields_by_name['prelu_param'].message_type = _PRELUCALIBRATIONPARAMETER
_CONVOLUTIONCALIBRATIONCALIBRATIONPARAMETER.fields_by_name['relu_param'].message_type = _RELUCALIBRATIONPARAMETER
_INNERPRODUCTCALIBRATIONPARAMETER.fields_by_name['prelu_param'].message_type = _PRELUCALIBRATIONPARAMETER
_LAYERCALIBRATIONPARAMETER.fields_by_name['blob_param'].message_type = _BLOBPARAMETER
_LAYERCALIBRATIONPARAMETER.fields_by_name['convolution_param'].message_type = _CONVOLUTIONCALIBRATIONCALIBRATIONPARAMETER
_LAYERCALIBRATIONPARAMETER.fields_by_name['inner_product_param'].message_type = _INNERPRODUCTCALIBRATIONPARAMETER
_LAYERCALIBRATIONPARAMETER.fields_by_name['pooling_param'].message_type = _POOLINGCALIBRATIONPARAMETER
_LAYERCALIBRATIONPARAMETER.fields_by_name['relu_param'].message_type = _RELUCALIBRATIONPARAMETER
_LAYERCALIBRATIONPARAMETER.fields_by_name['prelu_param'].message_type = _PRELUCALIBRATIONPARAMETER
_LAYERCALIBRATIONPARAMETER.fields_by_name['concat_param'].message_type = _CONCATCALIBRATIONPARAMETER
_LAYERCALIBRATIONPARAMETER.fields_by_name['leakyrelu_param'].message_type = _LEAKYRELUCALIBRATIONPARAMETER
_NETCALIBRATIONPARAMETER.fields_by_name['layer'].message_type = _LAYERCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['ConvolutionCalibrationCalibrationParameter'] = _CONVOLUTIONCALIBRATIONCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['InnerProductCalibrationParameter'] = _INNERPRODUCTCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['PoolingCalibrationParameter'] = _POOLINGCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['ReLUCalibrationParameter'] = _RELUCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['PReLUCalibrationParameter'] = _PRELUCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['ConcatCalibrationParameter'] = _CONCATCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['LeakyReLUCalibrationParameter'] = _LEAKYRELUCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['LayerCalibrationParameter'] = _LAYERCALIBRATIONPARAMETER
DESCRIPTOR.message_types_by_name['BlobParameter'] = _BLOBPARAMETER
DESCRIPTOR.message_types_by_name['NetCalibrationParameter'] = _NETCALIBRATIONPARAMETER

ConvolutionCalibrationCalibrationParameter = _reflection.GeneratedProtocolMessageType('ConvolutionCalibrationCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _CONVOLUTIONCALIBRATIONCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:ConvolutionCalibrationCalibrationParameter)
  ))
_sym_db.RegisterMessage(ConvolutionCalibrationCalibrationParameter)

InnerProductCalibrationParameter = _reflection.GeneratedProtocolMessageType('InnerProductCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _INNERPRODUCTCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:InnerProductCalibrationParameter)
  ))
_sym_db.RegisterMessage(InnerProductCalibrationParameter)

PoolingCalibrationParameter = _reflection.GeneratedProtocolMessageType('PoolingCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _POOLINGCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:PoolingCalibrationParameter)
  ))
_sym_db.RegisterMessage(PoolingCalibrationParameter)

ReLUCalibrationParameter = _reflection.GeneratedProtocolMessageType('ReLUCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _RELUCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:ReLUCalibrationParameter)
  ))
_sym_db.RegisterMessage(ReLUCalibrationParameter)

PReLUCalibrationParameter = _reflection.GeneratedProtocolMessageType('PReLUCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _PRELUCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:PReLUCalibrationParameter)
  ))
_sym_db.RegisterMessage(PReLUCalibrationParameter)

ConcatCalibrationParameter = _reflection.GeneratedProtocolMessageType('ConcatCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _CONCATCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:ConcatCalibrationParameter)
  ))
_sym_db.RegisterMessage(ConcatCalibrationParameter)

LeakyReLUCalibrationParameter = _reflection.GeneratedProtocolMessageType('LeakyReLUCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _LEAKYRELUCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:LeakyReLUCalibrationParameter)
  ))
_sym_db.RegisterMessage(LeakyReLUCalibrationParameter)

LayerCalibrationParameter = _reflection.GeneratedProtocolMessageType('LayerCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _LAYERCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:LayerCalibrationParameter)
  ))
_sym_db.RegisterMessage(LayerCalibrationParameter)

BlobParameter = _reflection.GeneratedProtocolMessageType('BlobParameter', (_message.Message,), dict(
  DESCRIPTOR = _BLOBPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:BlobParameter)
  ))
_sym_db.RegisterMessage(BlobParameter)

NetCalibrationParameter = _reflection.GeneratedProtocolMessageType('NetCalibrationParameter', (_message.Message,), dict(
  DESCRIPTOR = _NETCALIBRATIONPARAMETER,
  __module__ = 'bmnet.common_calibration_pb2'
  # @@protoc_insertion_point(class_scope:NetCalibrationParameter)
  ))
_sym_db.RegisterMessage(NetCalibrationParameter)


# @@protoc_insertion_point(module_scope)
