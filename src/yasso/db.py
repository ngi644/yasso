# encoding: utf-8

from sqlalchemy import engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension

Base = declarative_base()
Session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


def initdb(config):
    engine = engine_from_config(config, 'sqlalchemy.')
    Session.configure(bind=engine)
