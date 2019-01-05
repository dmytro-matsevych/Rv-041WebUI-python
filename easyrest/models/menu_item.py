"""
This module describe data model for "menu_item" table
"""

from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
)

from .meta import Base


class MenuItem(Base):
    """
    The data model of "menu_items" table
    Defines data structure of "menu_items" table
    """
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    ingredients = Column(Text)
    menu_id = Column(Integer, ForeignKey('menus.id'))
