from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column, Integer,String, Boolean,MetaData, BigInteger, ForeignKey, Numeric
from tinkoff.invest import Coupon

Base = declarative_base()
class CouponSqlData(Base):
    __tablename__='coupon'
    #id =  Column( Integer, primary_key=True, autoincrement=True)
    figi =  Column(String,  primary_key=True, doc='Figi-идентификатор инструмента.')
    coupon_date =  Column(String,  primary_key=True, doc='Тикер инструмента.')
    coupon_number =  Column(Integer,  doc='Isin-идентификатор инструмента.')
    fix_date =  Column(String,  doc='Класс-код (секция торгов).')
    pay_one_bond =  Column(Numeric,  doc='Размер купона')
    coupon_type =  Column(String,  doc='Валюта расчётов.')
    coupon_start_date =  Column(String,  doc='Коэффициент ставки риска длинной позиции по инструменту.')
    coupon_end_date =  Column(String,  doc='Коэффициент ставки риска короткой позиции по инструменту.')
    coupon_period =  Column(Integer,  doc='Ставка риска минимальной маржи в лонг. Подробнее: ставка риска в лонг')
    currency= Column(String, doc='Валюта')


    def date_splitter(self,bond_date):
        if '00:00:00+00:00' in str(bond_date):
            return str(bond_date)[:-len('00:00:00+00:00')]
        return str(bond_date)
    def money_value_splitter(self,money_value):
        if 'units' in str(money_value):
            sd=str(money_value)
            return float(sd[sd.index("units=")+len("units="):sd.index(", nano")]+"."+sd[sd.index("nano=")+len("nano="):sd.index(")")])
        return float(money_value)



    def __init__(self, coupon_data: Coupon):
        if not coupon_data:
            return
        self.figi=coupon_data.figi
        
        self.coupon_date=self.date_splitter(coupon_data.coupon_date)
        self.coupon_number=coupon_data.coupon_number
        self.fix_date=self.date_splitter(coupon_data.fix_date)
        sd =str(coupon_data.pay_one_bond)
        self.pay_one_bond=self.money_value_splitter(coupon_data.pay_one_bond)
        self.coupon_type=str(coupon_data.coupon_type.name)
        self.coupon_start_date=self.date_splitter(coupon_data.coupon_start_date)
        self.coupon_end_date=self.date_splitter(coupon_data.coupon_end_date)
        self.coupon_period=coupon_data.coupon_period
        self.currency=sd[sd.index("currency='")+len("currency='"):sd.index("',")]

        
    def create_tables(self,engine):
        Base.metadata.create_all(engine)