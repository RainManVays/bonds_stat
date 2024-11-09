from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, BigInteger, DateTime
from sqlalchemy.orm import relationship
from database import Base
from tinkoff.invest import Bond, Coupon
from datetime import datetime
from setup_logging import setup_logging
from tinkoff.invest.schemas import LastPrice
log= setup_logging()
    
class BondSqlData(Base):
    __tablename__ = 'bond'
    figi =  Column(String, primary_key=True,  doc='Figi-идентификатор инструмента.')
    date_insert =  Column(DateTime, primary_key=True,  doc='Дата добавления инструмента в базу')
    ticker =  Column(String,  doc='Тикер инструмента.')
    class_code =  Column(String,  doc='Класс-код (секция торгов).')
    isin =  Column(String,  doc='Isin-идентификатор инструмента.')
    lot =  Column(Integer,  doc='Лотность инструмента. Возможно совершение операций только на количества ценной бумаги, кратные параметру lot. Подробнее: лот')
    currency =  Column(String,  doc='Валюта расчётов.')
    klong =  Column(String,  doc='Коэффициент ставки риска длинной позиции по инструменту.')
    kshort =  Column(String,  doc='Коэффициент ставки риска короткой позиции по инструменту.')
    dlong =  Column(String,  doc='Ставка риска минимальной маржи в лонг. Подробнее: ставка риска в лонг')
    dshort =  Column(String,  doc='Ставка риска минимальной маржи в шорт. Подробнее: ставка риска в шорт')
    dlong_min =  Column(String,  doc='Ставка риска начальной маржи в лонг. Подробнее: ставка риска в лонг')
    dshort_min =  Column(String,  doc='Ставка риска начальной маржи в шорт. Подробнее: ставка риска в шорт')
    short_enabled_flag =  Column(Integer,  doc='Признак доступности для операций в шорт.')
    name =  Column(String,  doc='Название инструмента.')
    exchange =  Column(String,  doc='Торговая площадка.')
    coupon_quantity_per_year =  Column(Integer,  doc='Количество выплат по купонам в год.')
    maturity_date =  Column(String,  doc='Дата погашения облигации в часовом поясе UTC.')
    nominal =  Column(Numeric,  doc='Номинал облигации.')
    state_reg_date =  Column(String,  doc='Дата выпуска облигации в часовом поясе UTC.')
    placement_date =  Column(String,  doc='Дата размещения в часовом поясе UTC.')
    placement_price =  Column(String,  doc='Цена размещения.')
    aci_value =  Column(String,  doc='Значение НКД (накопленного купонного дохода) на дату.')
    country_of_risk =  Column(String,  doc='Код страны риска, т.е. страны, в которой компания ведёт основной бизнес.')
    country_of_risk_name =  Column(String,  doc='Наименование страны риска, т.е. страны, в которой компания ведёт основной бизнес.')
    sector =  Column(String,  doc='Сектор экономики.')
    issue_kind =  Column(String,  doc='Форма выпуска. Возможные значения: documentary — документарная; non_documentary — бездокументарная.')
    issue_size =  Column(BigInteger,  doc='Размер выпуска.')
    issue_size_plan =  Column(BigInteger,  doc='Плановый размер выпуска.')
    trading_status =  Column(String,  doc='Текущий режим торгов инструмента.')
    otc_flag =  Column(Integer,  doc='Признак внебиржевой ценной бумаги.')
    buy_available_flag =  Column(Integer,  doc='Признак доступности для покупки.')
    sell_available_flag =  Column(Integer,  doc='Признак доступности для продажи.')
    floating_coupon_flag =  Column(Integer,  doc='Признак облигации с плавающим купоном.')
    perpetual_flag =  Column(Integer,  doc='Признак бессрочной облигации.')
    amortization_flag =  Column(Integer,  doc='Признак облигации с амортизацией долга.')
    min_price_increment =  Column(String,  doc='Шаг цены.')
    api_trade_available_flag =  Column(Integer,  doc='Признак доступности торгов через API.')
    uid =  Column(String,  doc='Уникальный идентификатор инструмента.')

    def __init__(self,bond_data: Bond):
        if not bond_data:
            return
        self.figi= bond_data.figi
        self.date_insert = datetime.now()
        self.ticker= bond_data.ticker
        self.class_code= bond_data.class_code
        self.isin= bond_data.isin
        self.lot= bond_data.lot
        #self.currency= bond_data.currency
        self.klong= str(bond_data.klong)
        self.kshort= str(bond_data.kshort)
        self.dlong= str(bond_data.dlong)
        self.dshort= str(bond_data.dshort)
        self.dlong_min= str(bond_data.dlong_min)
        self.dshort_min= str(bond_data.dshort_min)
        self.short_enabled_flag= bond_data.short_enabled_flag
        self.name= bond_data.name
        self.exchange= bond_data.exchange
        self.coupon_quantity_per_year= bond_data.coupon_quantity_per_year
        self.maturity_date= str(bond_data.maturity_date)
        sd =str(bond_data.nominal)
        if "units=" in sd:
            self.nominal=float(sd[sd.index("units=")+len("units="):sd.index(", nano")]+"."+sd[sd.index("nano=")+len("nano="):sd.index(")")])
        else:
            self.nominal=sd
        self.currency=bond_data.currency

        self.state_reg_date= str(bond_data.state_reg_date)
        self.placement_date= str(bond_data.placement_date)
        self.placement_price= str(bond_data.placement_price)
        self.aci_value= str(bond_data.aci_value)
        self.country_of_risk= bond_data.country_of_risk
        self.country_of_risk_name= bond_data.country_of_risk_name
        self.sector= bond_data.sector
        self.issue_kind= bond_data.issue_kind
        self.issue_size= bond_data.issue_size
        self.issue_size_plan= bond_data.issue_size_plan
        self.trading_status= str(bond_data.trading_status)
        self.otc_flag= bond_data.otc_flag
        self.perpetual_flag= bond_data.perpetual_flag
        self.buy_available_flag= bond_data.buy_available_flag
        self.sell_available_flag= bond_data.sell_available_flag
        self.floating_coupon_flag= bond_data.floating_coupon_flag
        self.amortization_flag= (bond_data.amortization_flag)
        self.min_price_increment= str(bond_data.min_price_increment)
        self.api_trade_available_flag= (bond_data.api_trade_available_flag)
        self.uid= bond_data.uid
        
    def create_tables(self,engine):
        Base.metadata.create_all(engine)
    
    def get_json(self):
        return {
            "figi":self.figi,
            "placement_date":self.placement_date,
            "nominal":self.nominal,
            "currency":self.currency,
            "name":self.name,
            'coupon_quantity_per_year': self.coupon_quantity_per_year
        }



class CouponSqlData(Base):
    __tablename__='coupon'
    #id =  Column( Integer, primary_key=True, autoincrement=True)
    figi =  Column(String,  primary_key=True, doc='Figi-идентификатор инструмента.')
    date_insert =  Column(DateTime, primary_key=True,  doc='Дата добавления инструмента в базу')
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


class ObjectLastPrice(Base):
    __tablename__='object_last_price'
    figi =  Column(String,  primary_key=True, doc='Figi-идентификатор инструмента.')
    date_insert =  Column(DateTime, primary_key=True,  doc='Дата добавления инструмента в базу')
    price =  Column(String,  primary_key=True, doc='Тикер инструмента.')
    time =  Column(Integer,  doc='Isin-идентификатор инструмента.')
    instrument_uid =  Column(String,  doc='Класс-код (секция торгов).')


    def date_splitter(self,bond_date):
        if '00:00:00+00:00' in str(bond_date):
            return str(bond_date)[:-len('00:00:00+00:00')]
        return str(bond_date)
    def money_value_splitter(self,money_value):
        if 'units' in str(money_value):
            sd=str(money_value)
            return float(sd[sd.index("units=")+len("units="):sd.index(", nano")]+"."+sd[sd.index("nano=")+len("nano="):sd.index(")")])
        return float(money_value)



    def __init__(self, coupon_data: LastPrice):
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