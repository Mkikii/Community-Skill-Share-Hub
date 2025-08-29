from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///skillshare.db")
Session = sessionmaker(bind=engine)
session = Session()

# Import models so tables are created
from .user import User
from .skill import Skill
from .booking import Booking

Base.metadata.create_all(engine)
