from sqlalchemy.orm import sessionmaker
from models import db


def pega_sessao():
    Session = sessionmaker(bind=db) 
    session = Session()
    return session