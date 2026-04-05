from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

password = ""
SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:password@127.0.0.1:3306/cit_curriculum"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
