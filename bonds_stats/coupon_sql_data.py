from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column, Integer,String, Boolean,MetaData, BigInteger, ForeignKey, Numeric
from tinkoff.invest import Coupon

Base = declarative_base()
class CouponSqlData(Base):
    __tablename__='coupon'
    figi =  Column(String,  primary_key=True, doc='Figi-идентификатор инструмента.')
    coupon_date =  Column(String,  primary_key=True, doc='Тикер инструмента.')
    coupon_number =  Column(Integer,  doc='Isin-идентификатор инструмента.')
    fix_date =  Column(String,  doc='Класс-код (секция торгов).')
    pay_one_bond =  Column(String,  doc='Размер купона')
    coupon_type =  Column(String,  doc='Валюта расчётов.')
    coupon_start_date =  Column(String,  doc='Коэффициент ставки риска длинной позиции по инструменту.')
    coupon_end_date =  Column(String,  doc='Коэффициент ставки риска короткой позиции по инструменту.')
    coupon_period =  Column(Integer,  doc='Ставка риска минимальной маржи в лонг. Подробнее: ставка риска в лонг')
    currency= Column(String, doc='Валюта')

    def __init__(self, coupon_data: Coupon):
        if not coupon_data:
            return
        self.figi=coupon_data.figi
        sd =str(coupon_data.pay_one_bond)
        self.coupon_date=str(coupon_data.coupon_date)
        self.coupon_number=coupon_data.coupon_number
        self.fix_date=str(coupon_data.fix_date)
        self.pay_one_bond=str(float(sd[sd.index("units=")+len("units="):sd.index(", nano")]+"."+sd[sd.index("nano=")+len("nano="):sd.index(")")]))
        self.coupon_type=str(coupon_data.coupon_type)
        self.coupon_start_date=str(coupon_data.coupon_start_date)
        self.coupon_end_date=str(coupon_data.coupon_end_date)
        self.coupon_period=coupon_data.coupon_period
        self.currency=sd[sd.index("currency='")+len("currency='"):sd.index("',")]

        
    def create_tables(self,engine):
        Base.metadata.create_all(engine)