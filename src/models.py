import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    gender = Column(String(100))
    height_cm = Column(Integer)
    mass_kg = Column(Integer)
    eye_color = Column(String(100))
    hair_color = Column(String(100))
    skin_color = Column(String(100))
    url = Column(String(200), unique=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    population = Column(Integer)
    climate = Column(String(100))
    terrain = Column(String(100))
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    url = Column(String(200), unique=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    model = Column(String(100))
    passengers = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    cargo_capacity = Column(Integer)
    url = Column(String(200), unique=True)
    consumables = Column(String(100))
    vehicle_class = Column(String(100))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    username = Column(String(100))
    password = Column(String(100))

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
