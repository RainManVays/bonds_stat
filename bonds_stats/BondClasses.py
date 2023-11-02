from datetime import datetime, date

from tinkoff.invest.schemas import BondResponse, Coupon, PortfolioPosition
class BondStat:
    def __init__(self, bond_name, bonds_count, bond_curr_price:float, next_pay: float, coupons:dict, months: list) -> None:
        self.bond_name=bond_name
        self.bonds_count=bonds_count
        self.bond_curr_price=bond_curr_price
        self.coupons=coupons
        self.next_pay=next_pay
        if len(months)==12:
            self.months="All"
        else:
            self.months=months



class BondInfo:
     def __init__(self, bond: BondResponse, coupons: list) -> None:
        self.bond_figi= bond.instrument.figi
        self.bond_name=bond.instrument.name
        
        self.bond_curr_price=bond.instrument.nominal
        self.bond_nominal_price=bond.instrument.nominal
        self.bond_end_date=bond.instrument.maturity_date
        self.bond_coupon=""
        self.bond_month_payments=""
        self.percent=""
        self.fix_coupon= ""
        self.pay_period=bond.instrument.coupon_quantity_per_year
        self.amortization= bond.instrument.amortization_flag
        self.bond_infiniti= bond.instrument.perpetual_flag
        

class CouponInfo:
     def __init__(self, coupon: Coupon, bond_name: str) -> None:
          self.coupon_date=coupon.coupon_date
          self.coupon_number=coupon.coupon_number
          self.pay_one_bond=coupon.pay_one_bond
          self.coupon_type=coupon.coupon_type
          self.coupon_period=coupon.coupon_period

class BondPayResults:
        def __init__(self, total_amount_bonds, total_year_payment, count_bonds, bond_pay_dates:dict, bonds_stat:[BondStat]) -> None:
            self.total_amount_bonds= total_amount_bonds
            self.avg_money_for_month= f"avg money for month {(total_year_payment/12):.2f}"
            self.avg_roi= f"avg roi: {(total_year_payment/count_bonds*100):.2f}%"
            self.total_amount_bonds= total_amount_bonds
            self.total_money= f'total money for {datetime.now().year} year  : {total_year_payment:.2f} rub'
            self.bond_pay_dates= bond_pay_dates
            print(bond_pay_dates)
            self.bonds_stat=bonds_stat
