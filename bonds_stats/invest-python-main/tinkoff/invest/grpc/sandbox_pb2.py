# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/sandbox.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tinkoff.invest.grpc import common_pb2 as tinkoff_dot_invest_dot_grpc_dot_common__pb2
from tinkoff.invest.grpc import orders_pb2 as tinkoff_dot_invest_dot_grpc_dot_orders__pb2
from tinkoff.invest.grpc import operations_pb2 as tinkoff_dot_invest_dot_grpc_dot_operations__pb2
from tinkoff.invest.grpc import users_pb2 as tinkoff_dot_invest_dot_grpc_dot_users__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tinkoff/invest/grpc/sandbox.proto',
  package='tinkoff.public.invest.api.contract.v1',
  syntax='proto3',
  serialized_options=b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!tinkoff/invest/grpc/sandbox.proto\x12%tinkoff.public.invest.api.contract.v1\x1a tinkoff/invest/grpc/common.proto\x1a tinkoff/invest/grpc/orders.proto\x1a$tinkoff/invest/grpc/operations.proto\x1a\x1ftinkoff/invest/grpc/users.proto\"\x1b\n\x19OpenSandboxAccountRequest\"0\n\x1aOpenSandboxAccountResponse\x12\x12\n\naccount_id\x18\x01 \x01(\t\"0\n\x1a\x43loseSandboxAccountRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"\x1d\n\x1b\x43loseSandboxAccountResponse\"l\n\x13SandboxPayInRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x41\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"Z\n\x14SandboxPayInResponse\x12\x42\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue2\xae\x0c\n\x0eSandboxService\x12\x99\x01\n\x12OpenSandboxAccount\x12@.tinkoff.public.invest.api.contract.v1.OpenSandboxAccountRequest\x1a\x41.tinkoff.public.invest.api.contract.v1.OpenSandboxAccountResponse\x12\x8b\x01\n\x12GetSandboxAccounts\x12\x39.tinkoff.public.invest.api.contract.v1.GetAccountsRequest\x1a:.tinkoff.public.invest.api.contract.v1.GetAccountsResponse\x12\x9c\x01\n\x13\x43loseSandboxAccount\x12\x41.tinkoff.public.invest.api.contract.v1.CloseSandboxAccountRequest\x1a\x42.tinkoff.public.invest.api.contract.v1.CloseSandboxAccountResponse\x12\x85\x01\n\x10PostSandboxOrder\x12\x37.tinkoff.public.invest.api.contract.v1.PostOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x85\x01\n\x10GetSandboxOrders\x12\x37.tinkoff.public.invest.api.contract.v1.GetOrdersRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.GetOrdersResponse\x12\x8b\x01\n\x12\x43\x61ncelSandboxOrder\x12\x39.tinkoff.public.invest.api.contract.v1.CancelOrderRequest\x1a:.tinkoff.public.invest.api.contract.v1.CancelOrderResponse\x12\x86\x01\n\x14GetSandboxOrderState\x12;.tinkoff.public.invest.api.contract.v1.GetOrderStateRequest\x1a\x31.tinkoff.public.invest.api.contract.v1.OrderState\x12\x88\x01\n\x13GetSandboxPositions\x12\x37.tinkoff.public.invest.api.contract.v1.PositionsRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PositionsResponse\x12\x8b\x01\n\x14GetSandboxOperations\x12\x38.tinkoff.public.invest.api.contract.v1.OperationsRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.OperationsResponse\x12\x88\x01\n\x13GetSandboxPortfolio\x12\x37.tinkoff.public.invest.api.contract.v1.PortfolioRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PortfolioResponse\x12\x87\x01\n\x0cSandboxPayIn\x12:.tinkoff.public.invest.api.contract.v1.SandboxPayInRequest\x1a;.tinkoff.public.invest.api.contract.v1.SandboxPayInResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3'
  ,
  dependencies=[tinkoff_dot_invest_dot_grpc_dot_common__pb2.DESCRIPTOR,tinkoff_dot_invest_dot_grpc_dot_orders__pb2.DESCRIPTOR,tinkoff_dot_invest_dot_grpc_dot_operations__pb2.DESCRIPTOR,tinkoff_dot_invest_dot_grpc_dot_users__pb2.DESCRIPTOR,])




_OPENSANDBOXACCOUNTREQUEST = _descriptor.Descriptor(
  name='OpenSandboxAccountRequest',
  full_name='tinkoff.public.invest.api.contract.v1.OpenSandboxAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=215,
  serialized_end=242,
)


_OPENSANDBOXACCOUNTRESPONSE = _descriptor.Descriptor(
  name='OpenSandboxAccountResponse',
  full_name='tinkoff.public.invest.api.contract.v1.OpenSandboxAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='tinkoff.public.invest.api.contract.v1.OpenSandboxAccountResponse.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=244,
  serialized_end=292,
)


_CLOSESANDBOXACCOUNTREQUEST = _descriptor.Descriptor(
  name='CloseSandboxAccountRequest',
  full_name='tinkoff.public.invest.api.contract.v1.CloseSandboxAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='tinkoff.public.invest.api.contract.v1.CloseSandboxAccountRequest.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=294,
  serialized_end=342,
)


_CLOSESANDBOXACCOUNTRESPONSE = _descriptor.Descriptor(
  name='CloseSandboxAccountResponse',
  full_name='tinkoff.public.invest.api.contract.v1.CloseSandboxAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=344,
  serialized_end=373,
)


_SANDBOXPAYINREQUEST = _descriptor.Descriptor(
  name='SandboxPayInRequest',
  full_name='tinkoff.public.invest.api.contract.v1.SandboxPayInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='tinkoff.public.invest.api.contract.v1.SandboxPayInRequest.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='tinkoff.public.invest.api.contract.v1.SandboxPayInRequest.amount', index=1,
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
  ],
  serialized_start=375,
  serialized_end=483,
)


_SANDBOXPAYINRESPONSE = _descriptor.Descriptor(
  name='SandboxPayInResponse',
  full_name='tinkoff.public.invest.api.contract.v1.SandboxPayInResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='balance', full_name='tinkoff.public.invest.api.contract.v1.SandboxPayInResponse.balance', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=485,
  serialized_end=575,
)

_SANDBOXPAYINREQUEST.fields_by_name['amount'].message_type = tinkoff_dot_invest_dot_grpc_dot_common__pb2._MONEYVALUE
_SANDBOXPAYINRESPONSE.fields_by_name['balance'].message_type = tinkoff_dot_invest_dot_grpc_dot_common__pb2._MONEYVALUE
DESCRIPTOR.message_types_by_name['OpenSandboxAccountRequest'] = _OPENSANDBOXACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['OpenSandboxAccountResponse'] = _OPENSANDBOXACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['CloseSandboxAccountRequest'] = _CLOSESANDBOXACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['CloseSandboxAccountResponse'] = _CLOSESANDBOXACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['SandboxPayInRequest'] = _SANDBOXPAYINREQUEST
DESCRIPTOR.message_types_by_name['SandboxPayInResponse'] = _SANDBOXPAYINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenSandboxAccountRequest = _reflection.GeneratedProtocolMessageType('OpenSandboxAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENSANDBOXACCOUNTREQUEST,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OpenSandboxAccountRequest)
  })
_sym_db.RegisterMessage(OpenSandboxAccountRequest)

OpenSandboxAccountResponse = _reflection.GeneratedProtocolMessageType('OpenSandboxAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENSANDBOXACCOUNTRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.OpenSandboxAccountResponse)
  })
_sym_db.RegisterMessage(OpenSandboxAccountResponse)

CloseSandboxAccountRequest = _reflection.GeneratedProtocolMessageType('CloseSandboxAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSESANDBOXACCOUNTREQUEST,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CloseSandboxAccountRequest)
  })
_sym_db.RegisterMessage(CloseSandboxAccountRequest)

CloseSandboxAccountResponse = _reflection.GeneratedProtocolMessageType('CloseSandboxAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSESANDBOXACCOUNTRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CloseSandboxAccountResponse)
  })
_sym_db.RegisterMessage(CloseSandboxAccountResponse)

SandboxPayInRequest = _reflection.GeneratedProtocolMessageType('SandboxPayInRequest', (_message.Message,), {
  'DESCRIPTOR' : _SANDBOXPAYINREQUEST,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SandboxPayInRequest)
  })
_sym_db.RegisterMessage(SandboxPayInRequest)

SandboxPayInResponse = _reflection.GeneratedProtocolMessageType('SandboxPayInResponse', (_message.Message,), {
  'DESCRIPTOR' : _SANDBOXPAYINRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.sandbox_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.SandboxPayInResponse)
  })
_sym_db.RegisterMessage(SandboxPayInResponse)


DESCRIPTOR._options = None

_SANDBOXSERVICE = _descriptor.ServiceDescriptor(
  name='SandboxService',
  full_name='tinkoff.public.invest.api.contract.v1.SandboxService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=578,
  serialized_end=2160,
  methods=[
  _descriptor.MethodDescriptor(
    name='OpenSandboxAccount',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.OpenSandboxAccount',
    index=0,
    containing_service=None,
    input_type=_OPENSANDBOXACCOUNTREQUEST,
    output_type=_OPENSANDBOXACCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSandboxAccounts',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.GetSandboxAccounts',
    index=1,
    containing_service=None,
    input_type=tinkoff_dot_invest_dot_grpc_dot_users__pb2._GETACCOUNTSREQUEST,
    output_type=tinkoff_dot_invest_dot_grpc_dot_users__pb2._GETACCOUNTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseSandboxAccount',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.CloseSandboxAccount',
    index=2,
    containing_service=None,
    input_type=_CLOSESANDBOXACCOUNTREQUEST,
    output_type=_CLOSESANDBOXACCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostSandboxOrder',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.PostSandboxOrder',
    index=3,
    containing_service=None,
    input_type=tinkoff_dot_invest_dot_grpc_dot_orders__pb2._POSTORDERREQUEST,
    output_type=tinkoff_dot_invest_dot_grpc_dot_orders__pb2._POSTORDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSandboxOrders',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.GetSandboxOrders',
    index=4,
    containing_service=None,
    input_type=tinkoff_dot_invest_dot_grpc_dot_orders__pb2._GETORDERSREQUEST,
    output_type=tinkoff_dot_invest_dot_grpc_dot_orders__pb2._GETORDERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CancelSandboxOrder',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.CancelSandboxOrder',
    index=5,
    containing_service=None,
    input_type=tinkoff_dot_invest_dot_grpc_dot_orders__pb2._CANCELORDERREQUEST,
    output_type=tinkoff_dot_invest_dot_grpc_dot_orders__pb2._CANCELORDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSandboxOrderState',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.GetSandboxOrderState',
    index=6,
    containing_service=None,
    input_type=tinkoff_dot_invest_dot_grpc_dot_orders__pb2._GETORDERSTATEREQUEST,
    output_type=tinkoff_dot_invest_dot_grpc_dot_orders__pb2._ORDERSTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSandboxPositions',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.GetSandboxPositions',
    index=7,
    containing_service=None,
    input_type=tinkoff_dot_invest_dot_grpc_dot_operations__pb2._POSITIONSREQUEST,
    output_type=tinkoff_dot_invest_dot_grpc_dot_operations__pb2._POSITIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSandboxOperations',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.GetSandboxOperations',
    index=8,
    containing_service=None,
    input_type=tinkoff_dot_invest_dot_grpc_dot_operations__pb2._OPERATIONSREQUEST,
    output_type=tinkoff_dot_invest_dot_grpc_dot_operations__pb2._OPERATIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSandboxPortfolio',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.GetSandboxPortfolio',
    index=9,
    containing_service=None,
    input_type=tinkoff_dot_invest_dot_grpc_dot_operations__pb2._PORTFOLIOREQUEST,
    output_type=tinkoff_dot_invest_dot_grpc_dot_operations__pb2._PORTFOLIORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SandboxPayIn',
    full_name='tinkoff.public.invest.api.contract.v1.SandboxService.SandboxPayIn',
    index=10,
    containing_service=None,
    input_type=_SANDBOXPAYINREQUEST,
    output_type=_SANDBOXPAYINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SANDBOXSERVICE)

DESCRIPTOR.services_by_name['SandboxService'] = _SANDBOXSERVICE

# @@protoc_insertion_point(module_scope)
