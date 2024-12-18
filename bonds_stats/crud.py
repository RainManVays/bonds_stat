from datetime import datetime, timedelta
from models import BondSqlData, CouponSqlData
from database import SessionLocal
from tinkoff.invest.schemas import Bond

from setup_logging import setup_logging
log= setup_logging()

# Create
def create_bond(bond_data: Bond) -> BondSqlData:
    session = SessionLocal()
    try:
        bond = BondSqlData(bond_data)
        session.add(bond)
        session.commit()
        session.refresh(bond)
        return bond
    finally:
        session.close()

# Read (get one bond by primary key)
def get_bond(figi: str, date_insert: str) -> BondSqlData:
    session = SessionLocal()
    try:
        return session.query(BondSqlData).filter(
            BondSqlData.figi == figi,
            BondSqlData.date_insert == date_insert
        ).first()
    finally:
        session.close()


def get_bond_figi_on_name(bond_name:str):
    session = SessionLocal()
    try:
        return session.query(BondSqlData).filter(
            BondSqlData.name==bond_name
        ).first().figi
    finally:
        session.close()




# Read (get all bonds)
def get_all_bonds() -> list[BondSqlData]:
    #[figi[0] for figi in s.query(BondSqlData.figi)]
    session = SessionLocal()
    try:
        bonds = session.query(BondSqlData).all()
        log.debug(f"selected bonds count {len(bonds)}")
        return bonds
    finally:
        session.close()

# Update
def update_bond(figi: str, date_insert: str, updates: dict) -> BondSqlData:
    session = SessionLocal()
    try:
        bond = session.query(BondSqlData).filter(
            BondSqlData.figi == figi,
            BondSqlData.date_insert == date_insert
        ).first()
        
        if bond:
            for key, value in updates.items():
                setattr(bond, key, value)
            session.commit()
            session.refresh(bond)
        
        return bond
    finally:
        session.close()

# Delete
def delete_bond(figi: str, date_insert: str) -> bool:
    session = SessionLocal()
    try:
        bond = session.query(BondSqlData).filter(
            BondSqlData.figi == figi,
            BondSqlData.date_insert == date_insert
        ).first()
        
        if bond:
            session.delete(bond)
            session.commit()
            return True
        
        return False
    finally:
        session.close()
        
def delete_all_bonds():
    session = SessionLocal()
    try:
        # Удаляем все записи в таблице bond
        deleted_rows = session.query(BondSqlData).delete()
        session.commit()
        log.debug(f"Удалено {deleted_rows} записей из таблицы bond.")
    except Exception as e:
        session.rollback()
        log.debug(f"Ошибка при удалении всех записей: {e}")
    finally:
        session.close()


def delete_old_bonds(days_old: int):
    session = SessionLocal()
    try:
        # Определяем дату отсечения
        cutoff_date = datetime.now() - timedelta(days=days_old)

        # Удаляем записи, которые старше указанного числа дней
        deleted_rows = session.query(BondSqlData).filter(BondSqlData.date_insert < cutoff_date).delete()
        session.commit()
        log.debug(f"Удалено {deleted_rows} записей, старше {days_old} дней.")
    except Exception as e:
        session.rollback()
        log.debug(f"Ошибка при удалении записей: {e}")
    finally:
        session.close()



# Create
def create_coupon(coupon_data: dict) -> CouponSqlData:
    session = SessionLocal()
    coupon = CouponSqlData(**coupon_data)
    session.add(coupon)
    session.commit()
    session.refresh(coupon)
    return coupon

# Read (get one coupon by primary key)
def get_coupon(figi: str, coupon_date: str) -> CouponSqlData:
    session = SessionLocal()
    return session.query(CouponSqlData).filter(
        CouponSqlData.figi == figi,
        CouponSqlData.coupon_date == coupon_date
    ).first()

# Read (get all coupons)
def get_all_coupons() -> list[CouponSqlData]:
    session = SessionLocal()
    return session.query(CouponSqlData).all()

# Update
def update_coupon(figi: str, coupon_date: str, updates: dict) -> CouponSqlData:
    session = SessionLocal()
    coupon = session.query(CouponSqlData).filter(
        CouponSqlData.figi == figi,
        CouponSqlData.coupon_date == coupon_date
    ).first()
    
    if coupon:
        for key, value in updates.items():
            setattr(coupon, key, value)
        session.commit()
        session.refresh(coupon)
    
    return coupon

# Delete
def delete_coupon(figi: str, coupon_date: str) -> bool:
    session = SessionLocal()
    coupon = session.query(CouponSqlData).filter(
        CouponSqlData.figi == figi,
        CouponSqlData.coupon_date == coupon_date
    ).first()
    
    if coupon:
        session.delete(coupon)
        session.commit()
        return True
    
    return False