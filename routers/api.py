from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.crud import (
    get_clientes, get_cliente, create_cliente,
    get_productos, get_producto, create_producto,
    get_ventas, get_venta, create_venta,
    get_detalles_ventas, get_detalle_venta, create_detalle_venta
)
from models.schemas import (
    ClienteCreate, ClienteOut,
    ProductoCreate, ProductoOut,
    VentaCreate, VentaOut,
    DetalleVentaCreate, DetalleVentaOut
)
from services.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas para Clientes
@router.get("/clientes", response_model=list[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return get_clientes(db)

@router.post("/clientes", response_model=ClienteOut)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return create_cliente(db, cliente)

# Rutas para Productos
@router.get("/productos", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return get_productos(db)

@router.post("/productos", response_model=ProductoOut)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return create_producto(db, producto)

# Rutas para Ventas
@router.get("/ventas", response_model=list[VentaOut])
def listar_ventas(db: Session = Depends(get_db)):
    return get_ventas(db)

@router.post("/ventas", response_model=VentaOut)
def crear_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    return create_venta(db, venta)

# Rutas para Detalles de Ventas
@router.get("/detalles-ventas", response_model=list[DetalleVentaOut])
def listar_detalles_ventas(db: Session = Depends(get_db)):
    return get_detalles_ventas(db)

@router.post("/detalles-ventas", response_model=DetalleVentaOut)
def crear_detalle_venta(detalle: DetalleVentaCreate, db: Session = Depends(get_db)):
    return create_detalle_venta(db, detalle)