from datetime import date, datetime
from BondClasses import BondStat, CouponInfo, BondInfo
from tinkoff.invest import Client, BondResponse, PortfolioResponse, PortfolioPosition, InstrumentIdType, GetBondCouponsResponse
from time import sleep

class BondInvestFacade:

    def __init__(self, token) -> None:
        self.token = token
        self.broker_bonds=[]


    

    def get_bond_name(self, bond_figi):
        if len(self.broker_bonds)>0:
            for bond in self.broker_bonds:
                if bond.figi == bond_figi:
                    return bond.name
                
        with Client(self.token) as client:
            self.broker_bonds = client.instruments.bonds().instruments
            for bond in self.broker_bonds:
                if bond.figi == bond_figi:
                    return bond.name

    def get_start_date(self):
        start_date = date(datetime.now().year,1,1)
        return datetime.combine(start_date, datetime.min.time())
    
    def get_end_date(self):
        end_date = date(datetime.now().year,12,31)
        return datetime.combine(end_date, datetime.min.time())


    def get_all_accounts(self):
        with Client(self.token) as client:
            accounts = client.users.get_accounts()
            for acc in accounts.accounts:
                print(acc)
            

    def get_all_bonds(self):      
        bonds_stat=[] 
        with Client(self.token) as client:
            bonds = client.instruments.bonds().instruments
            for bond in bonds:
                bonds_stat.append(BondInfo(bond,self.get_bond_coupon(bond.figi,self.get_start_date(), self.get_end_date())))

        return bonds_stat

    def get_bond_coupon(self, figi:str, start_date, end_date) -> list:
        coupons=[]
        sleep(0.3)
        with Client(self.token) as client:
            for coupon in client.instruments.get_bond_coupons(figi=figi,from_= start_date, to=end_date).events:
                coupons.append(CouponInfo(coupon=coupon, bond_figi=figi))
        return coupons