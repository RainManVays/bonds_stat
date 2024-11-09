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

def treeview_sort(tree, col, reverse):
    # получаем все значения столбцов в виде отдельного списка
    l = [(tree.set(k, col), k) for k in tree.get_children("")]
    # сортируем список
    l.sort(reverse=reverse)
    # переупорядочиваем значения в отсортированном порядке
    for index,  (_, k) in enumerate(l):
        tree.move(k, "", index)
    # в следующий раз выполняем сортировку в обратном порядке
    tree.heading(col, command=lambda: treeview_sort(tree,col, not reverse))