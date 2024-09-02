from datetime import datetime, date
from bond_invest_facade import *
import share_methods as sm
from tinkoff.invest.schemas import BondResponse, Coupon, PortfolioPosition, Bond

class BondStat:
    def __init__(self, bond_figi, bond_name, bonds_count, bond_curr_price:float, next_pay: float, coupons:dict, months: list,end_date:str) -> None:
        self.bond_figi=bond_figi
        self.bond_name=bond_name
        self.bonds_count=bonds_count
        self.bond_curr_price=bond_curr_price
        self.coupons=coupons
        self.next_pay=next_pay
        self.bond_end_date=end_date
        if len(months)==12:
            self.months="All"
        else:
            self.months=months



class BondInfo:
    def __init__(self, bond: Bond, coupons: list[Coupon]) -> None:
        self.bond_figi=bond.figi
        self.bond_name=bond.name
        
        self.bond_curr_price=sm.money_value_to_float(bond.nominal) 
        self.bond_nominal_price=sm.money_value_to_float(bond.nominal) 
        self.bond_end_date=bond.maturity_date
        self.bond_coupon=self.get_first_coupon_in_current_year(coupons)
        self.bond_month_payments=self.get_current_year_coupon_months(coupons)
        self.percent=self.get_percent(sm.money_value_to_float(bond.nominal),coupons)
        self.percent_on_nominal=self.get_percent(sm.money_value_to_float(bond.nominal),coupons)
        self.fix_coupon=bond.floating_coupon_flag
        self.pay_period=bond.coupon_quantity_per_year
        self.amortization=bond.amortization_flag
        self.bond_infiniti=bond.perpetual_flag
        self.coupons=coupons
        
    def get_current_year_coupon_months(self,coupons:list[Coupon]) -> list:
        month_list=[]
        for coupon in coupons:
            if coupon.coupon_date.year==datetime.now().year:
                month_list.append(coupon.coupon_date.month)
        return month_list

    def get_first_coupon_in_current_year(self,coupons:list[Coupon]) -> float:
        for coupon in coupons:
            if coupon.coupon_date.year==datetime.now().year:
                return sm.money_value_to_float(coupon.pay_one_bond)
    
    def get_percent(self,bond_price:float,coupons:list[Coupon]) -> float:
        coupons_in_current_year=0.0
        for coupon in coupons:
            if coupon.coupon_date.year==datetime.now().year:
                coupons_in_current_year+=sm.money_value_to_float(coupon.pay_one_bond)
        if float(bond_price)>0 and coupons_in_current_year >0:
            return f"{float(coupons_in_current_year/float(bond_price)*100):.2f}"
        return 0.0



class CouponInfo:
     def __init__(self, coupon: Coupon, bond_figi:str) -> None:
          self.bond_figi=bond_figi
          self.coupon_date=coupon.coupon_date
          self.coupon_number=coupon.coupon_number
          self.pay_one_bond=sm.money_value_to_float(coupon.pay_one_bond)
          self.coupon_type=coupon.coupon_type
          self.coupon_period=coupon.coupon_period
          

class BondPayResults:
    def __init__(self, total_amount_bonds, total_year_payment, count_bonds, bond_pay_dates:dict, bonds_stat:[BondStat]):
        self.total_amount_bonds=total_amount_bonds
        self.avg_money_for_month = f"avg money for month {(total_year_payment/12):.2f}"
        self.avg_roi= f"avg roi: {(total_year_payment/count_bonds*100):.2f}%"
        self.total_amount_bonds= total_amount_bonds
        self.total_money= f'total money for {datetime.now().year} year  : {total_year_payment:.2f} rub'
        self.bond_pay_dates= bond_pay_dates
        self.bonds_stat=bonds_stat
