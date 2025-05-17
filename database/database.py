from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2


engine = create_engine("postgresql+psycopg2://postgres:postgres@0.0.0.0:5437/pomodoro")

Session = sessionmaker(engine)


def get_db_session() -> Session:
    return Session
