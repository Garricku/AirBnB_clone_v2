#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade="all, delete, delete-orphan", backref="state"
                          )

    @property
    def cities(self):
        """
        Returns the list of City instances with state_id equals to the
        current State.id
        """
        if models.storage.__class__.__name__ == 'DBStoage':
            city_inst = models.DBstorage.all('City')
            return [city for city in city_inst.values()]
        else:
            city_instances = models.storage.all("City")
            return [city for city in city_instances.values()
                    if city.state_id == self.id]
