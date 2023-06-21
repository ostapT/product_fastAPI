from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.engine import Base


class DBProductType(Base):
    __tablename__ = "product_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(511), nullable=False)


class DBProduct(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(511), nullable=False)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    product_type_id = Column(Integer, ForeignKey("product_type.id"))

    product_type = relationship(DBProductType)
