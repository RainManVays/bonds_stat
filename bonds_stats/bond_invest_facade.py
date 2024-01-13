import configparser
from datetime import date, datetime
from BondClasses import BondStat, CouponInfo, BondInfo
from tinkoff.invest import Client, BondResponse, PortfolioResponse, PortfolioPosition, InstrumentIdType, GetBondCouponsResponse, OperationState, OperationType
from time import sleep


config= configparser.ConfigParser()
config.read('config.ini')

class BondInvestFacade:

    def __init__(self, token) -> None:
        self.token = token
        self.broker_bonds=[]
        self.accounts={}


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
        if self.accounts:
            return self.accounts
        with Client(self.token) as client:
            accounts = client.users.get_accounts()
            for acc in accounts.accounts:
                self.accounts[acc.name]=acc.id
                
        return self.accounts
    
    def get_account_id_on_name(self, account_name:str):
        return self.accounts[account_name]


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
    
    def get_coupon_payments(self,current_account:str, date_start, date_end):
        pay_result=[]
        if not date_start:
            date_start= self.get_start_date()
        if not date_end:
            date_end=self.get_end_date()
        with Client(self.token) as client:
            
            operations = client.operations.get_operations(account_id=current_account,from_=date_start, to=date_end, state=OperationState(1))
            for operation in operations.operations:
                if operation.operation_type == OperationType(23):
                    
                    bond_name = self.get_bond_name(operation.figi)
                    pay_date = operation.date
                    pay_sum = operation.payment.units
                    pay_result.append([bond_name,pay_date,pay_sum])

        return  pay_result
        
