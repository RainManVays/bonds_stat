from datetime import datetime
import configparser
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from .models import CouponSqlData, BondSqlData

config= configparser.ConfigParser()
config.read('config.ini')

DATABASE_URL=config['DEFAULT']["DATABASE_URL"]
from setup_logging import setup_logging
log= setup_logging()

#выпилить и перенести логику в crud
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

def get_bond_figi_from_database() -> list:
    s = Session()
    return [figi[0] for figi in s.query(BondSqlData.figi)]

def get_all_bonds_from_database() -> list:
    s = Session()
    return [bond for bond in s.query(BondSqlData).filter_by(buy_available_flag=1).order_by(BondSqlData.coupon_quantity_per_year)]

def get_bond_from_database(figi:str) -> BondSqlData:
    s = Session()
    return [bond for bond in s.query(BondSqlData).filter_by(buy_available_flag=1,figi=figi).order_by(BondSqlData.coupon_quantity_per_year)][0]


def get_bond_max_reg_date()-> str:
    s = Session()
    max_state_reg_date= s.query(func.max(BondSqlData.state_reg_date)).scalar()
    return max_state_reg_date

def get_bond_figi_without_coupon_from_database() -> list:
    s = Session()
    bonds_figi= set()
    coupons_figi=set()
    for figi in s.query(BondSqlData.figi):
        bonds_figi.add(figi[0])
    for coupon_figi in s.query(CouponSqlData.figi):
        coupons_figi.add(coupon_figi[0])
    return list(bonds_figi-coupons_figi)
