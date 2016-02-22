# encoding: utf-8

import cryptacular.bcrypt
from sqlalchemy import Column, Integer, String
from yasso.db import Session, Base

crypt = cryptacular.bcrypt.BCRYPTPasswordManager()


def hash_password(password):
    return unicode(crypt.encode(password))


class User(Base):
    __tablename__ = 'users'
    query = Session.query_property()

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    password = Column(String(255))

    def __init__(self, name, password, roll):
        self.name = name
        self.set_password(password)
        self.roll = roll

    def set_password(self, password):
        self.password = hash_password(password)

    def check_password(self, password):
        hashed_passwd = hash_password(password)
        return self.password == hashed_passwd
