"""Provides database storage"""

import os

import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

__all__ = ['RulesDB', 'Session']

engine = sqlalchemy.create_engine(os.getenv('DATABASE_URL'))
DatabaseObject = declarative_base(bind=engine, name='DatabaseObject')
DatabaseObject.__table_args__ = {'extend_existing': True}


class CtxSession(Session):
    """Allows sessions to be used as context managers and asynchronous context managers."""
    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, err_type, err, tb):
        if err_type is None:
            self.commit()
        else:
            self.rollback()
        return False

    async def __aexit__(self, err_type, err, tb):
        return self.__exit__(err_type, err, tb)


class RulesDB(DatabaseObject):
    __tablename__ = 'rules'
    rule_id = Column(String, primary_key=True)
    rule_text = Column(String)


DatabaseObject.metadata.create_all()
Session = sessionmaker(bind=engine, class_=CtxSession)
