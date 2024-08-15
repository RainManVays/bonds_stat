from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

DATABASE_URL=config['DEFAULT']["DATABASE_URL"]



engine = create_engine(DATABASE_URL, echo=True)

SessionLocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()