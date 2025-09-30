from sqlalchemy.orm import Session
from models.item import Item
from models.database_models import Cliente, Producto, Venta, DetalleVenta
from models.schemas import ClienteCreate, ProductoCreate, VentaCreate, DetalleVentaCreate

def get_items(db:Session):
    return db.query(Item).all()

# CRUD para Cliente
def get_clientes(db: Session):
    return db.query(Cliente).all()

def get_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def create_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# CRUD para Producto
def get_productos(db: Session):
    return db.query(Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# CRUD para Venta
def get_ventas(db: Session):
    return db.query(Venta).all()

def get_venta(db: Session, venta_id: int):
    return db.query(Venta).filter(Venta.id == venta_id).first()

def create_venta(db: Session, venta: VentaCreate):
    db_venta = Venta(**venta.dict())
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return db_venta

# CRUD para DetalleVenta
def get_detalles_ventas(db: Session):
    return db.query(DetalleVenta).all()

def get_detalle_venta(db: Session, detalle_id: int):
    return db.query(DetalleVenta).filter(DetalleVenta.id == detalle_id).first()

def create_detalle_venta(db: Session, detalle: DetalleVentaCreate):
    db_detalle = DetalleVenta(**detalle.dict())
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle