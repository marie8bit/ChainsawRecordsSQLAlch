from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from base import Base
class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    catches = Column(Integer)

    def __repr__(self):
        return 'Record: ID: {} Record Holder = {} Country = {} catches = {}'.format(self.id, self.name, self.country, self.catches)
