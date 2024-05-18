from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column, Integer,String, Boolean,MetaData, BigInteger, ForeignKey, Numeric, DateTime
from tinkoff.invest import Bond
from datetime import datetime
Base = declarative_base()
class BondSqlData(Base):
    __tablename__='bond'
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


        
