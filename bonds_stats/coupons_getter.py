from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from bond_data import BondSqlData
from coupon_data import CouponSqlData
from sqlalchemy import create_engine,func

engine = create_engine("sqlite:///bonds/bonds_db.sqlite", echo=True)

Session = sessionmaker(bind=engine)

def get_coupons_from_bond(bond_figi:str) -> list:
    s = Session()
    return [coupon for coupon in s.query(CouponSqlData).filter_by(figi=bond_figi)]

