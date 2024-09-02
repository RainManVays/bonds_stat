from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

DATABASE_URL=config['DEFAULT']["DATABASE_URL"]


print(f"engine create database {DATABASE_URL}")
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    inspector = inspect(engine)

    # Если таблиц нет, создаем их
    if not inspector.get_table_names():
        import models  # Импортируем модели
        Base.metadata.create_all(bind=engine)
    else:
        print("Таблицы уже существуют в базе данных")