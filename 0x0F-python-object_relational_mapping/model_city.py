#!/usr/bin/python3
"""
Declarative mapper module
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Declarative mapping for `cities` table
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
