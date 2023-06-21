from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import schemas
from db import models


async def get_all_product_types(db: AsyncSession):
    query = select(models.DBProductType)
    result = await db.execute(query)
    return result.scalars().all()


async def get_product_type_by_name(db: AsyncSession, name: str):
    query = select(models.DBProductType).where(
        models.DBProductType.name == name
    )
    result = await db.execute(query)
    return result.scalars().first()


async def create_product_type(
    db: AsyncSession, product_type: schemas.ProductTypeCreate
):
    db_product_type = models.DBProductType(
        name=product_type.name, description=product_type.description
    )
    db.add(db_product_type)
    await db.commit()
    await db.refresh(db_product_type)

    return db_product_type


async def retrieve_product_type(db: AsyncSession, product_type_id: int):
    query = select(models.DBProductType).where(
        models.DBProductType.id == product_type_id
    )
    result = await db.execute(query)
    return result.scalars().first()


async def get_all_products(db: AsyncSession):
    query = select(models.DBProduct)
    result = db.execute(query)
    return result.scalars().all()


async def create_product(db: AsyncSession, product: schemas.ProductCreate):
    db_product = models.DBProduct(
        name=product.name,
        description=product.description,
        price=product.price,
        product_type_id=product.product_type_id,
    )
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)

    return db_product


async def retrieve_product(db: AsyncSession, product_id: int):
    query = select(models.DBProduct).where(
        models.DBProductType.id == product_id
    )
    result = await db.execute(query)
    return result.scalars().first()
