from datetime import datetime, date
class BondStat:
    def __init__(self, bond_name, bonds_count, bond_curr_price:float, next_pay: float, coupons:dict) -> None:
        self.bond_name=bond_name
        self.bonds_count=bonds_count
        self.bond_curr_price=bond_curr_price
        self.coupons=coupons
        self.next_pay=next_pay

class BondPayResults:
        def __init__(self, total_amount_bonds, total_year_payment, count_bonds, bond_pay_dates:dict, bonds_stat:[BondStat]) -> None:
            self.total_amount_bonds= total_amount_bonds
            self.avg_money_for_month= f"avg money for month {(total_year_payment/12):.2f}"
            self.avg_roi= f"avg roi: {(total_year_payment/count_bonds*100):.2f}%"
            self.total_amount_bonds= total_amount_bonds
            self.total_money= f'total money for {datetime.now().year} year  : {total_year_payment:.2f} rub'
            self.bond_pay_dates= bond_pay_dates
            self.bonds_stat=bonds_stat
