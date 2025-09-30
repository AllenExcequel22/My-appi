from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

# Schema base para Cliente
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

# Schema base para Producto
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

# Schema base para Venta
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

# Schema base para DetalleVenta
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
    nombre: str  # Changed from 'title' to 'nombre'
    description: str | None = None  # Fixed typo
    price: float | None = Field(None, ge=0)

class ItemCreate(ItemBase):
    nombre: str  # Changed from 'title' to 'nombre'
    price: float

class ItemUpdate(BaseModel):
    pass

class ItemOut(ItemBase):
    id: int
    nombre: str | None  # Changed from 'title' to 'nombre'
    created_at: datetime  # Fixed typo
    description: str  # Fixed typo
    price: float

    model_config = {"from_attributes": True}  # Fixed typo


