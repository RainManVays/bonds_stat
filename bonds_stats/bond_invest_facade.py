import configparser
from datetime import date, datetime
import time
from BondClasses import BondStat, CouponInfo, BondInfo
from tinkoff.invest import Client, BondResponse, PortfolioResponse, PortfolioPosition, InstrumentIdType, GetBondCouponsResponse, OperationState, OperationType
from time import sleep
from models import BondSqlData, CouponSqlData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
config= configparser.ConfigParser()
config.read('config.ini')

class BondInvestFacade:

    CURRENT_ACCOUNT=""
    
    def __init__(self, token) -> None:
        self.token = token
        self.broker_bonds=[]
        self.accounts={}
        self.engine = create_engine("sqlite:///bonds_db.sqlite")


    def get_bond_name(self, bond_figi):
        if len(self.broker_bonds)>0:
            for bond in self.broker_bonds:
                if bond_figi in bond.figi:
                    return bond.name
        else:
            with Client(self.token) as client:
                self.broker_bonds = client.instruments.bonds().instruments
                for bond in self.broker_bonds:
                    if bond_figi in bond.figi:
                        return bond.name
                    
    def get_bond_maturity_date(self, bond_figi):
        if len(self.broker_bonds)>0:
            for bond in self.broker_bonds:
                if bond_figi in bond.figi:
                    return bond.maturity_date
        else:
            with Client(self.token) as client:
                self.broker_bonds = client.instruments.bonds().instruments
                for bond in self.broker_bonds:
                    if bond_figi in bond.figi:
                        return bond.maturity_date


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
    
    def get_current_account(self):
        return BondInvestFacade.CURRENT_ACCOUNT
    
    def set_current_account(self,current_account):
        BondInvestFacade.CURRENT_ACCOUNT=current_account


    def get_bonds_from_tcs(self):
        black_list_invalid_bonds =['BBG001CYCG37','TCS878009866']
        print('get bonds from TCS')
        with Client(self.token) as client:
            bonds_sql_list=[]
            for bond in client.instruments.bonds().instruments:
                if bond.figi in black_list_invalid_bonds:
                    continue
                bonds_sql_list.append(BondSqlData(bond))
                print(f"{bond.name} {bond.coupon_quantity_per_year}")
            print(f'TCS bonds count {len(bonds_sql_list)}')
            return bonds_sql_list



    def update_db_bonds(self,engine):
        print('update bonds')
        Session = sessionmaker(bind=engine)
        BondSqlData(None).create_tables(engine)
        s = Session()
        tcs_bonds=self.get_bonds_from_tcs()
        db_bonds = [figi[0] for figi in s.query(BondSqlData.figi)]
        if len(db_bonds)==0:
            print('0 bonds in database add all bonds from tcs')
            
            s.add_all(tcs_bonds)
            s.commit()
            s.close()
            return

        for tcs_bond in tcs_bonds:
            if tcs_bond.figi not in db_bonds:
                s.add(BondSqlData(tcs_bond))
                print(f'append new bond {tcs_bond.name}  date rep: {tcs_bond.state_reg_date}')
            s.commit()
            s.close()



    def get_coupon_from_tcs(self,bond_figi:str,start_date=datetime(1970,1,1,1,1,1,1), end_date=datetime(2050,1,1,1,1,1)):
        
        self.update_db_coupons(self.engine,[bond_figi])
        
        
        Session = sessionmaker(bind=self.engine)
        s = Session()
        db_coupons = [coupon for coupon in s.query(CouponSqlData)]
        """
        сделать
        получаем купоны из базы
        если купонов 0
        получаем фулл из ткс пишем в базу
        если date_insert больше чем сутки, обновляем на дельту в сутки
    
        """
        
        
        coupon_sql_list=[]
        with Client(self.token) as client:
            print(f'get coupon for figi: {bond_figi}')
            for coupon in client.instruments.get_bond_coupons(figi=bond_figi,from_=start_date,to=end_date).events:
                if coupon.figi != bond_figi:
                    print(f'coupon figi {coupon.figi} not equals bond figi {bond_figi} and will be replaced')
                    coupon.figi=bond_figi
                coupon_sql_list.append(CouponSqlData(coupon))            
                print(f"new coupon figi: {coupon.figi} date: {coupon.coupon_date} pay size: {coupon.pay_one_bond}")
        return coupon_sql_list


    def update_db_coupons(self,engine,bonds_figi:list,start_date='', end_date=''):
        CouponSqlData(None).create_tables(engine)
        Session = sessionmaker(bind=engine)
        s = Session()
        exc_count= 0
        for figi in bonds_figi:
            while True:
                try:
                    coupons= self.get_coupon_from_tcs(figi)
                    break
                except Exception as ex:
                    print("TCS cry abour rate limit, wait 60 sec and repeat")
                    print(ex)
                    time.sleep(60)
                    exc_count+=1
                    if exc_count>=10:
                        raise Exception('count TCS rate limit errors more than 10, stop working')

            s.add_all(coupons)
            print(f'add new coupons in bond {figi}')
            s.commit()
            time.sleep(15)
        s.close()


    def get_all_bonds(self):      
        bonds_stat=[] 
        #self.update_db_bonds(self.engine)
        with Client(self.token) as client:
            bonds = client.instruments.bonds().instruments
            for bond in bonds:
                bonds_stat.append(BondInfo(bond,self.get_bond_coupon(bond.figi,self.get_start_date(), self.get_end_date())))

        return bonds_stat

    def get_bond_coupon(self, figi:str, start_date, end_date) -> list:
        #self.update_db_coupons()
        coupons=[]
        sleep(0.3)
        with Client(self.token) as client:
            for coupon in client.instruments.get_bond_coupons(figi=figi,from_= start_date, to=end_date).events:
                coupons.append(CouponInfo(coupon=coupon, bond_figi=figi))
        return coupons
    
    def get_coupon_payments(self,current_account:str, date_start, date_end):
        pay_result=[]
        if not date_start:
            date_start = self.get_start_date()
        if not date_end:
            date_end = self.get_end_date()
        with Client(self.token) as client:
            
            operations = client.operations.get_operations(account_id=current_account,from_=date_start, to=date_end, state=OperationState(1))
            
            for operation in operations.operations:
                if operation.operation_type == OperationType(23):
                    
                    bond_name = self.get_bond_name(operation.figi)
                    pay_date = operation.date
                    pay_sum = operation.payment.units
                    pay_result.append([bond_name,pay_date,pay_sum])
        pay_result.sort(key=lambda x: x[1])
        return  pay_result
        
