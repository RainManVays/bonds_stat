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

