from sqlalchemy import Column, Integer, String, DateTime
from base import Base

import datetime
import json

class Student(Base):
    """ Student Class """

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    username = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def to_dict(self):
        """ Returns a dictionary representation of the Student """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def to_json(self):
        """ Returns a JSON representation of the Student """
        return json.dumps(self.to_dict())


        