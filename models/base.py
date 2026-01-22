# models/tea.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#  TeaModel extends SQLAlchemy's Base class.
#  Extending Base lets SQLAlchemy 'know' about our model, so it can use it.

class BaseModel(Base):

    # This will be used directly to make a
    # TABLE in Postgresql
    # __tablename__ = "teas". there is no table on base model
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    crated_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

