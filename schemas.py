from datetime import datetime

from pydantic import BaseModel


class ProductTypeBase(BaseModel):
    name: str
    description: str


class ProductTypeCreate(ProductTypeBase):
    pass


class ProductTypeUpdate(ProductTypeBase):
    pass


class ProductType(ProductTypeBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    product_type_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
