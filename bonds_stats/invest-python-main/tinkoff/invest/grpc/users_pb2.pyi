"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import tinkoff.invest.grpc.common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AccountType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _AccountTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AccountType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ACCOUNT_TYPE_UNSPECIFIED: _AccountType.ValueType  # 0
    """Тип аккаунта не определён."""

    ACCOUNT_TYPE_TINKOFF: _AccountType.ValueType  # 1
    """Брокерский счёт Тинькофф."""

    ACCOUNT_TYPE_TINKOFF_IIS: _AccountType.ValueType  # 2
    """ИИС счёт."""

    ACCOUNT_TYPE_INVEST_BOX: _AccountType.ValueType  # 3
    """Инвесткопилка."""

class AccountType(_AccountType, metaclass=_AccountTypeEnumTypeWrapper):
    """Тип счёта."""
    pass

ACCOUNT_TYPE_UNSPECIFIED: AccountType.ValueType  # 0
"""Тип аккаунта не определён."""

ACCOUNT_TYPE_TINKOFF: AccountType.ValueType  # 1
"""Брокерский счёт Тинькофф."""

ACCOUNT_TYPE_TINKOFF_IIS: AccountType.ValueType  # 2
"""ИИС счёт."""

ACCOUNT_TYPE_INVEST_BOX: AccountType.ValueType  # 3
"""Инвесткопилка."""

global___AccountType = AccountType


class _AccountStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _AccountStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AccountStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ACCOUNT_STATUS_UNSPECIFIED: _AccountStatus.ValueType  # 0
    """Статус счёта не определён."""

    ACCOUNT_STATUS_NEW: _AccountStatus.ValueType  # 1
    """Новый, в процессе открытия."""

    ACCOUNT_STATUS_OPEN: _AccountStatus.ValueType  # 2
    """Открытый и активный счёт."""

    ACCOUNT_STATUS_CLOSED: _AccountStatus.ValueType  # 3
    """Закрытый счёт."""

class AccountStatus(_AccountStatus, metaclass=_AccountStatusEnumTypeWrapper):
    """Статус счёта."""
    pass

ACCOUNT_STATUS_UNSPECIFIED: AccountStatus.ValueType  # 0
"""Статус счёта не определён."""

ACCOUNT_STATUS_NEW: AccountStatus.ValueType  # 1
"""Новый, в процессе открытия."""

ACCOUNT_STATUS_OPEN: AccountStatus.ValueType  # 2
"""Открытый и активный счёт."""

ACCOUNT_STATUS_CLOSED: AccountStatus.ValueType  # 3
"""Закрытый счёт."""

global___AccountStatus = AccountStatus


class _AccessLevel:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _AccessLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AccessLevel.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ACCOUNT_ACCESS_LEVEL_UNSPECIFIED: _AccessLevel.ValueType  # 0
    """Уровень доступа не определён."""

    ACCOUNT_ACCESS_LEVEL_FULL_ACCESS: _AccessLevel.ValueType  # 1
    """Полный доступ к счёту."""

    ACCOUNT_ACCESS_LEVEL_READ_ONLY: _AccessLevel.ValueType  # 2
    """Доступ с уровнем прав "только чтение"."""

    ACCOUNT_ACCESS_LEVEL_NO_ACCESS: _AccessLevel.ValueType  # 3
    """Доступ отсутствует."""

class AccessLevel(_AccessLevel, metaclass=_AccessLevelEnumTypeWrapper):
    """Уровень доступа к счёту."""
    pass

ACCOUNT_ACCESS_LEVEL_UNSPECIFIED: AccessLevel.ValueType  # 0
"""Уровень доступа не определён."""

ACCOUNT_ACCESS_LEVEL_FULL_ACCESS: AccessLevel.ValueType  # 1
"""Полный доступ к счёту."""

ACCOUNT_ACCESS_LEVEL_READ_ONLY: AccessLevel.ValueType  # 2
"""Доступ с уровнем прав "только чтение"."""

ACCOUNT_ACCESS_LEVEL_NO_ACCESS: AccessLevel.ValueType  # 3
"""Доступ отсутствует."""

global___AccessLevel = AccessLevel


class GetAccountsRequest(google.protobuf.message.Message):
    """Запрос получения счетов пользователя."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___GetAccountsRequest = GetAccountsRequest

class GetAccountsResponse(google.protobuf.message.Message):
    """Список счетов пользователя."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNTS_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Account]:
        """Массив счетов клиента."""
        pass
    def __init__(self,
        *,
        accounts: typing.Optional[typing.Iterable[global___Account]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts",b"accounts"]) -> None: ...
global___GetAccountsResponse = GetAccountsResponse

class Account(google.protobuf.message.Message):
    """Информация о счёте."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    OPENED_DATE_FIELD_NUMBER: builtins.int
    CLOSED_DATE_FIELD_NUMBER: builtins.int
    ACCESS_LEVEL_FIELD_NUMBER: builtins.int
    id: typing.Text
    """Идентификатор счёта."""

    type: global___AccountType.ValueType
    """Тип счёта."""

    name: typing.Text
    """Название счёта."""

    status: global___AccountStatus.ValueType
    """Статус счёта."""

    @property
    def opened_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата открытия счёта в часовом поясе UTC."""
        pass
    @property
    def closed_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата закрытия счёта в часовом поясе UTC."""
        pass
    access_level: global___AccessLevel.ValueType
    """Уровень доступа к текущему счёту (определяется токеном)."""

    def __init__(self,
        *,
        id: typing.Text = ...,
        type: global___AccountType.ValueType = ...,
        name: typing.Text = ...,
        status: global___AccountStatus.ValueType = ...,
        opened_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        closed_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        access_level: global___AccessLevel.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["closed_date",b"closed_date","opened_date",b"opened_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_level",b"access_level","closed_date",b"closed_date","id",b"id","name",b"name","opened_date",b"opened_date","status",b"status","type",b"type"]) -> None: ...
global___Account = Account

class GetMarginAttributesRequest(google.protobuf.message.Message):
    """Запрос маржинальных показателей по счёту"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    account_id: typing.Text
    """Идентификатор счёта пользователя."""

    def __init__(self,
        *,
        account_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["account_id",b"account_id"]) -> None: ...
global___GetMarginAttributesRequest = GetMarginAttributesRequest

class GetMarginAttributesResponse(google.protobuf.message.Message):
    """Маржинальные показатели по счёту."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LIQUID_PORTFOLIO_FIELD_NUMBER: builtins.int
    STARTING_MARGIN_FIELD_NUMBER: builtins.int
    MINIMAL_MARGIN_FIELD_NUMBER: builtins.int
    FUNDS_SUFFICIENCY_LEVEL_FIELD_NUMBER: builtins.int
    AMOUNT_OF_MISSING_FUNDS_FIELD_NUMBER: builtins.int
    @property
    def liquid_portfolio(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Ликвидная стоимость портфеля. Подробнее: [что такое ликвидный портфель?](https://help.tinkoff.ru/margin-trade/short/liquid-portfolio/)."""
        pass
    @property
    def starting_margin(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Начальная маржа — начальное обеспечение для совершения новой сделки. Подробнее: [начальная и минимальная маржа](https://help.tinkoff.ru/margin-trade/short/initial-and-maintenance-margin/)."""
        pass
    @property
    def minimal_margin(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Минимальная маржа — это минимальное обеспечение для поддержания позиции, которую вы уже открыли. Подробнее: [начальная и минимальная маржа](https://help.tinkoff.ru/margin-trade/short/initial-and-maintenance-margin/)."""
        pass
    @property
    def funds_sufficiency_level(self) -> tinkoff.invest.grpc.common_pb2.Quotation:
        """Уровень достаточности средств. Соотношение стоимости ликвидного портфеля к начальной марже."""
        pass
    @property
    def amount_of_missing_funds(self) -> tinkoff.invest.grpc.common_pb2.MoneyValue:
        """Объем недостающих средств. Разница между стартовой маржой и ликвидной стоимости портфеля."""
        pass
    def __init__(self,
        *,
        liquid_portfolio: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        starting_margin: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        minimal_margin: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        funds_sufficiency_level: typing.Optional[tinkoff.invest.grpc.common_pb2.Quotation] = ...,
        amount_of_missing_funds: typing.Optional[tinkoff.invest.grpc.common_pb2.MoneyValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["amount_of_missing_funds",b"amount_of_missing_funds","funds_sufficiency_level",b"funds_sufficiency_level","liquid_portfolio",b"liquid_portfolio","minimal_margin",b"minimal_margin","starting_margin",b"starting_margin"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount_of_missing_funds",b"amount_of_missing_funds","funds_sufficiency_level",b"funds_sufficiency_level","liquid_portfolio",b"liquid_portfolio","minimal_margin",b"minimal_margin","starting_margin",b"starting_margin"]) -> None: ...
global___GetMarginAttributesResponse = GetMarginAttributesResponse

class GetUserTariffRequest(google.protobuf.message.Message):
    """Запрос текущих лимитов пользователя."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___GetUserTariffRequest = GetUserTariffRequest

class GetUserTariffResponse(google.protobuf.message.Message):
    """Текущие лимиты пользователя."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UNARY_LIMITS_FIELD_NUMBER: builtins.int
    STREAM_LIMITS_FIELD_NUMBER: builtins.int
    @property
    def unary_limits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UnaryLimit]:
        """Массив лимитов пользователя по unary-запросам"""
        pass
    @property
    def stream_limits(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StreamLimit]:
        """Массив лимитов пользователей для stream-соединений"""
        pass
    def __init__(self,
        *,
        unary_limits: typing.Optional[typing.Iterable[global___UnaryLimit]] = ...,
        stream_limits: typing.Optional[typing.Iterable[global___StreamLimit]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stream_limits",b"stream_limits","unary_limits",b"unary_limits"]) -> None: ...
global___GetUserTariffResponse = GetUserTariffResponse

class UnaryLimit(google.protobuf.message.Message):
    """Лимит unary-методов."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LIMIT_PER_MINUTE_FIELD_NUMBER: builtins.int
    METHODS_FIELD_NUMBER: builtins.int
    limit_per_minute: builtins.int
    """Количество unary-запросов в минуту"""

    @property
    def methods(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Названия методов"""
        pass
    def __init__(self,
        *,
        limit_per_minute: builtins.int = ...,
        methods: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["limit_per_minute",b"limit_per_minute","methods",b"methods"]) -> None: ...
global___UnaryLimit = UnaryLimit

class StreamLimit(google.protobuf.message.Message):
    """Лимит stream-соединений."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LIMIT_FIELD_NUMBER: builtins.int
    STREAMS_FIELD_NUMBER: builtins.int
    limit: builtins.int
    """Максимальное количество stream-соединений"""

    @property
    def streams(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Названия stream-методов"""
        pass
    def __init__(self,
        *,
        limit: builtins.int = ...,
        streams: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["limit",b"limit","streams",b"streams"]) -> None: ...
global___StreamLimit = StreamLimit

class GetInfoRequest(google.protobuf.message.Message):
    """Запрос информации о пользователе."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___GetInfoRequest = GetInfoRequest

class GetInfoResponse(google.protobuf.message.Message):
    """Информация о пользователе."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PREM_STATUS_FIELD_NUMBER: builtins.int
    QUAL_STATUS_FIELD_NUMBER: builtins.int
    QUALIFIED_FOR_WORK_WITH_FIELD_NUMBER: builtins.int
    TARIFF_FIELD_NUMBER: builtins.int
    prem_status: builtins.bool
    """Признак премиум клиента."""

    qual_status: builtins.bool
    """Признак квалифицированного инвестора."""

    @property
    def qualified_for_work_with(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Набор требующих тестирования инструментов и возможностей, с которыми может работать пользователь."""
        pass
    tariff: typing.Text
    """Наименование тарифа пользователя."""

    def __init__(self,
        *,
        prem_status: builtins.bool = ...,
        qual_status: builtins.bool = ...,
        qualified_for_work_with: typing.Optional[typing.Iterable[typing.Text]] = ...,
        tariff: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["prem_status",b"prem_status","qual_status",b"qual_status","qualified_for_work_with",b"qualified_for_work_with","tariff",b"tariff"]) -> None: ...
global___GetInfoResponse = GetInfoResponse
