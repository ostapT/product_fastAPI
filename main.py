from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import crud
import schemas
from db.engine import get_async_session

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get(
    "/product_types/",
    response_model=list[schemas.ProductType]
)
async def read_all_product_types(
        db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_all_product_types(db=db)


@app.post(
    "/product_types/",
    response_model=schemas.ProductType
)
async def create_product_type(
        product_type: schemas.ProductTypeCreate,
        db: AsyncSession = Depends(get_async_session)
):
    db_product_type = await crud.get_product_type_by_name(
        db=db,
        name=product_type.name
    )

    if db_product_type:
        raise HTTPException(
            status_code=400,
            detail="Such name for Product Type already exists"
        )

    return await crud.create_product_type(
        db=db,
        product_type=product_type
    )


@app.get(
    "/product_types/{product_type_id}",
    response_model=schemas.ProductType
)
async def read_product_type_by_id(
        product_type_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    db_product_type = await crud.retrieve_product_type(
        db=db,
        product_type_id=product_type_id
    )

    if not db_product_type:
        raise HTTPException(
            status_code=404,
            detail="Product Type not found"
        )

    return db_product_type


@app.put(
    "/product_types/{product_type_id}",
    response_model=schemas.ProductType
)
async def update_product_type(
        product_type_id: int,
        product_type: schemas.ProductTypeUpdate,
        db: AsyncSession = Depends(get_async_session)
):

    db_product_type = await crud.retrieve_product_type(
        db=db,
        product_type_id=product_type_id
    )
    if not db_product_type:
        raise HTTPException(
            status_code=404,
            detail="Product Type not found"
        )

    for field, value in product_type.dict(exclude_unset=True).items():
        setattr(db_product_type, field, value)

    await db.commit()
    await db.refresh(db_product_type)
    return db_product_type


@app.delete("/product_types/{product_type_id}")
async def delete_product_type(
        product_type_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    db_product_type = await crud.retrieve_product_type(
        db=db,
        product_type_id=product_type_id
    )
    if not db_product_type:
        raise HTTPException(
            status_code=404,
            detail="Product Type not found"
        )
    await db.delete(db_product_type)
    await db.commit()

    return {"message": "Product Type deleted"}


@app.get(
    "/products/",
    response_model=list[schemas.Product]
)
async def read_all_products(
        db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_all_products(db=db)


@app.post("/products/", response_model=schemas.Product)
async def create_product(
        product: schemas.ProductCreate,
        db: AsyncSession = Depends(get_async_session)
):
    return await crud.create_product(db=db, product=product)


@app.get(
    "/products/{product_id}",
    response_model=schemas.Product
)
async def read_product_by_id(
        product_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    db_product = await crud.retrieve_product(
        db=db,
        product_id=product_id
    )

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return db_product


@app.put(
    "/products/{product_id}",
    response_model=schemas.Product
)
async def update_product(
        product_id: int,
        product: schemas.ProductUpdate,
        db: AsyncSession = Depends(get_async_session)
):
    db_product = await crud.retrieve_product(
        db=db,
        product_id=product_id
    )
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    for field, value in product.dict(exclude_unset=True).items():
        setattr(db_product, field, value)

    await db.commit()
    await db.refresh(db_product)
    return db_product


@app.delete("/products/{product_id}")
async def delete_product(
        product_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    db_product = await crud.retrieve_product(
        db=db,
        product_id=product_id
    )
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    await db.delete(db_product)
    await db.commit()

    return {"message": "Product deleted"}
