"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import tinkoff.invest.grpc.common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class OpenSandboxAccountRequest(google.protobuf.message.Message):
    """Запрос открытия счёта в песочнице.
    пустой запрос
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___OpenSandboxAccountRequest = OpenSandboxAccountRequest

class OpenSandboxAccountResponse(google.protobuf.message.Message):
    """Номер открытого счёта в песочнице."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Номер счёта"""

    def __init__(self,
        *,
        account_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id"]) -> None: ...
global___OpenSandboxAccountResponse = OpenSandboxAccountResponse

class CloseSandboxAccountRequest(google.protobuf.message.Message):
    """Запрос закрытия счёта в песочнице."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Номер счёта"""

    def __init__(self,
        *,
        account_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id"]) -> None: ...
global___CloseSandboxAccountRequest = CloseSandboxAccountRequest

class CloseSandboxAccountResponse(google.protobuf.message.Message):
    """Результат закрытия счёта в песочнице.
    пустой ответ
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___CloseSandboxAccountResponse = CloseSandboxAccountResponse

class SandboxPayInRequest(google.protobuf.message.Message):
    """Запрос пополнения счёта в песочнице."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Номер счёта"""

    @property
    def amount(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Сумма пополнения счёта в рублях"""
        pass
    def __init__(self,
        *,
        account_id: typing.Text = ...,
        amount: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["amount",b"amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id","amount",b"amount"]) -> None: ...
global___SandboxPayInRequest = SandboxPayInRequest

class SandboxPayInResponse(google.protobuf.message.Message):
    """Результат пополнения счёта, текущий баланс."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BALANCE_FIELD_NUMBER: builtins.int
    @property
    def balance(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Текущий баланс счёта"""
        pass
    def __init__(self,
        *,
        balance: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["balance",b"balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["balance",b"balance"]) -> None: ...
global___SandboxPayInResponse = SandboxPayInResponse
