from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./groups.db"
SQLALCHEMY_DATABASE_URL = "postgresql://ancuimfw:R6DRmXPpv3gAf_1Jmf2Cig6WZtg2FzoY@drona.db.elephantsql.com/ancuimfw"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, #connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()