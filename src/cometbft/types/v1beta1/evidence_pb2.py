# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/types/v1beta1/evidence.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cometbft.types.v1beta1 import types_pb2 as cometbft_dot_types_dot_v1beta1_dot_types__pb2
from cometbft.types.v1beta1 import validator_pb2 as cometbft_dot_types_dot_v1beta1_dot_validator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cometbft/types/v1beta1/evidence.proto',
  package='cometbft.types.v1beta1',
  syntax='proto3',
  serialized_options=b'Z7github.com/cometbft/cometbft/api/cometbft/types/v1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%cometbft/types/v1beta1/evidence.proto\x12\x16\x63ometbft.types.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"cometbft/types/v1beta1/types.proto\x1a&cometbft/types/v1beta1/validator.proto\"\xbe\x01\n\x08\x45vidence\x12P\n\x17\x64uplicate_vote_evidence\x18\x01 \x01(\x0b\x32-.cometbft.types.v1beta1.DuplicateVoteEvidenceH\x00\x12Y\n\x1clight_client_attack_evidence\x18\x02 \x01(\x0b\x32\x31.cometbft.types.v1beta1.LightClientAttackEvidenceH\x00\x42\x05\n\x03sum\"\xe1\x01\n\x15\x44uplicateVoteEvidence\x12,\n\x06vote_a\x18\x01 \x01(\x0b\x32\x1c.cometbft.types.v1beta1.Vote\x12,\n\x06vote_b\x18\x02 \x01(\x0b\x32\x1c.cometbft.types.v1beta1.Vote\x12\x1a\n\x12total_voting_power\x18\x03 \x01(\x03\x12\x17\n\x0fvalidator_power\x18\x04 \x01(\x03\x12\x37\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\"\x87\x02\n\x19LightClientAttackEvidence\x12=\n\x11\x63onflicting_block\x18\x01 \x01(\x0b\x32\".cometbft.types.v1beta1.LightBlock\x12\x15\n\rcommon_height\x18\x02 \x01(\x03\x12?\n\x14\x62yzantine_validators\x18\x03 \x03(\x0b\x32!.cometbft.types.v1beta1.Validator\x12\x1a\n\x12total_voting_power\x18\x04 \x01(\x03\x12\x37\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\"H\n\x0c\x45videnceList\x12\x38\n\x08\x65vidence\x18\x01 \x03(\x0b\x32 .cometbft.types.v1beta1.EvidenceB\x04\xc8\xde\x1f\x00\x42\x39Z7github.com/cometbft/cometbft/api/cometbft/types/v1beta1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,cometbft_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,cometbft_dot_types_dot_v1beta1_dot_validator__pb2.DESCRIPTOR,])




_EVIDENCE = _descriptor.Descriptor(
  name='Evidence',
  full_name='cometbft.types.v1beta1.Evidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='duplicate_vote_evidence', full_name='cometbft.types.v1beta1.Evidence.duplicate_vote_evidence', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='light_client_attack_evidence', full_name='cometbft.types.v1beta1.Evidence.light_client_attack_evidence', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='sum', full_name='cometbft.types.v1beta1.Evidence.sum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=197,
  serialized_end=387,
)


_DUPLICATEVOTEEVIDENCE = _descriptor.Descriptor(
  name='DuplicateVoteEvidence',
  full_name='cometbft.types.v1beta1.DuplicateVoteEvidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vote_a', full_name='cometbft.types.v1beta1.DuplicateVoteEvidence.vote_a', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_b', full_name='cometbft.types.v1beta1.DuplicateVoteEvidence.vote_b', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_voting_power', full_name='cometbft.types.v1beta1.DuplicateVoteEvidence.total_voting_power', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_power', full_name='cometbft.types.v1beta1.DuplicateVoteEvidence.validator_power', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cometbft.types.v1beta1.DuplicateVoteEvidence.timestamp', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\220\337\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=390,
  serialized_end=615,
)


_LIGHTCLIENTATTACKEVIDENCE = _descriptor.Descriptor(
  name='LightClientAttackEvidence',
  full_name='cometbft.types.v1beta1.LightClientAttackEvidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='conflicting_block', full_name='cometbft.types.v1beta1.LightClientAttackEvidence.conflicting_block', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='common_height', full_name='cometbft.types.v1beta1.LightClientAttackEvidence.common_height', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='byzantine_validators', full_name='cometbft.types.v1beta1.LightClientAttackEvidence.byzantine_validators', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_voting_power', full_name='cometbft.types.v1beta1.LightClientAttackEvidence.total_voting_power', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cometbft.types.v1beta1.LightClientAttackEvidence.timestamp', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\220\337\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=618,
  serialized_end=881,
)


_EVIDENCELIST = _descriptor.Descriptor(
  name='EvidenceList',
  full_name='cometbft.types.v1beta1.EvidenceList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='evidence', full_name='cometbft.types.v1beta1.EvidenceList.evidence', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=883,
  serialized_end=955,
)

_EVIDENCE.fields_by_name['duplicate_vote_evidence'].message_type = _DUPLICATEVOTEEVIDENCE
_EVIDENCE.fields_by_name['light_client_attack_evidence'].message_type = _LIGHTCLIENTATTACKEVIDENCE
_EVIDENCE.oneofs_by_name['sum'].fields.append(
  _EVIDENCE.fields_by_name['duplicate_vote_evidence'])
_EVIDENCE.fields_by_name['duplicate_vote_evidence'].containing_oneof = _EVIDENCE.oneofs_by_name['sum']
_EVIDENCE.oneofs_by_name['sum'].fields.append(
  _EVIDENCE.fields_by_name['light_client_attack_evidence'])
_EVIDENCE.fields_by_name['light_client_attack_evidence'].containing_oneof = _EVIDENCE.oneofs_by_name['sum']
_DUPLICATEVOTEEVIDENCE.fields_by_name['vote_a'].message_type = cometbft_dot_types_dot_v1beta1_dot_types__pb2._VOTE
_DUPLICATEVOTEEVIDENCE.fields_by_name['vote_b'].message_type = cometbft_dot_types_dot_v1beta1_dot_types__pb2._VOTE
_DUPLICATEVOTEEVIDENCE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LIGHTCLIENTATTACKEVIDENCE.fields_by_name['conflicting_block'].message_type = cometbft_dot_types_dot_v1beta1_dot_types__pb2._LIGHTBLOCK
_LIGHTCLIENTATTACKEVIDENCE.fields_by_name['byzantine_validators'].message_type = cometbft_dot_types_dot_v1beta1_dot_validator__pb2._VALIDATOR
_LIGHTCLIENTATTACKEVIDENCE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVIDENCELIST.fields_by_name['evidence'].message_type = _EVIDENCE
DESCRIPTOR.message_types_by_name['Evidence'] = _EVIDENCE
DESCRIPTOR.message_types_by_name['DuplicateVoteEvidence'] = _DUPLICATEVOTEEVIDENCE
DESCRIPTOR.message_types_by_name['LightClientAttackEvidence'] = _LIGHTCLIENTATTACKEVIDENCE
DESCRIPTOR.message_types_by_name['EvidenceList'] = _EVIDENCELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Evidence = _reflection.GeneratedProtocolMessageType('Evidence', (_message.Message,), {
  'DESCRIPTOR' : _EVIDENCE,
  '__module__' : 'cometbft.types.v1beta1.evidence_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.types.v1beta1.Evidence)
  })
_sym_db.RegisterMessage(Evidence)

DuplicateVoteEvidence = _reflection.GeneratedProtocolMessageType('DuplicateVoteEvidence', (_message.Message,), {
  'DESCRIPTOR' : _DUPLICATEVOTEEVIDENCE,
  '__module__' : 'cometbft.types.v1beta1.evidence_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.types.v1beta1.DuplicateVoteEvidence)
  })
_sym_db.RegisterMessage(DuplicateVoteEvidence)

LightClientAttackEvidence = _reflection.GeneratedProtocolMessageType('LightClientAttackEvidence', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTCLIENTATTACKEVIDENCE,
  '__module__' : 'cometbft.types.v1beta1.evidence_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.types.v1beta1.LightClientAttackEvidence)
  })
_sym_db.RegisterMessage(LightClientAttackEvidence)

EvidenceList = _reflection.GeneratedProtocolMessageType('EvidenceList', (_message.Message,), {
  'DESCRIPTOR' : _EVIDENCELIST,
  '__module__' : 'cometbft.types.v1beta1.evidence_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.types.v1beta1.EvidenceList)
  })
_sym_db.RegisterMessage(EvidenceList)


DESCRIPTOR._options = None
_DUPLICATEVOTEEVIDENCE.fields_by_name['timestamp']._options = None
_LIGHTCLIENTATTACKEVIDENCE.fields_by_name['timestamp']._options = None
_EVIDENCELIST.fields_by_name['evidence']._options = None
# @@protoc_insertion_point(module_scope)