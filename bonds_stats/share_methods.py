from tinkoff.invest.schemas import MoneyValue
from setup_logging import setup_logging
log= setup_logging()

def money_units_nano_to_float(units, nano):
    return f"{float(f'{units}.{nano}'):.2f}"

def money_value_to_float(money: MoneyValue) -> float:
    log.debug(money)
    if type(money) == str:
        return float(money)
    return f"{float(f'{money.units}.{money.nano}'):.2f}"
