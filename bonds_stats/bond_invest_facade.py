from BondClasses import BondStat
from tinkoff.invest import Client, BondResponse, PortfolioResponse, PortfolioPosition, InstrumentIdType, GetBondCouponsResponse


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

    def get_all_bonds(self):
        bond_pay_dates={}
        total_year_payment=0.0
        
        
        bonds_stat=[] 
        with Client(self.token) as client:
            accounts = client.users.get_accounts()
            
            print(accounts)
            bonds =  client.instruments.bonds().instruments
            for bond in bonds:
                bonds_stat.append(BondStat(bond_name=bond.name,bonds_count=0,bond_curr_price=1,next_pay=0,coupons={},months=[]))

        return bonds_stat