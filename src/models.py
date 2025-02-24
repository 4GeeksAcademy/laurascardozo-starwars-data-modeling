import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum as sqlalchemy_enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum

Base = declarative_base()

class MediaEnum(Enum):
    PHOTO = "PHOTO"
    VIDEO = "VIDEO"

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    planet = relationship("planet", backref="user")
    character = relationship("character", backref="user")
    favorite = relationship("favorite", backref="user")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    favorite = relationship("favorite", backref="planet")
    media = relationship("media", backref="planet")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    favorite = relationship("favorite", backref="character")
    media = relationship("media", backref="character")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    mediatype = Column(sqlalchemy_enum(MediaEnum))
    url = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character = Column(Integer, ForeignKey("character.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')