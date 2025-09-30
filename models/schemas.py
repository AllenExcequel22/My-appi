from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ClienteBase(BaseModel):
    uuid: str
    nombre: str
    email: str
    rut: str


class ClienteCreate(ClienteBase):
    pass


class ClienteOut(ClienteBase):
    id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True


class ProductoBase(BaseModel):
    uuid: str
    nombre: str
    categoria: str
    precio: int


class ProductoCreate(ProductoBase):
    pass


class ProductoOut(ProductoBase):
    id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True


class VentaBase(BaseModel):
    uuid: str
    fecha: datetime
    total: int
    cliente_id: int


class VentaCreate(VentaBase):
    pass


class VentaOut(VentaBase):
    id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True


class DetalleVentaBase(BaseModel):
    uuid: str
    producto_id: int
    venta_id: int
    precio: int
    descuento: int
    cantidad: int


class DetalleVentaCreate(DetalleVentaBase):
    pass


class DetalleVentaOut(DetalleVentaBase):
    id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    nombre: str
    description: str | None = None
    price: float | None = Field(None, ge=0)


class ItemCreate(ItemBase):
    nombre: str
    price: float


class ItemUpdate(BaseModel):
    pass


class ItemOut(ItemBase):
    id: int
    nombre: str | None
    created_at: datetime
    description: str
    price: float

    model_config = {"from_attributes": True}


