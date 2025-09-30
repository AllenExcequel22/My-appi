from datetime import datetime
from fastapi import FastAPI
from sqlalchemy.orm import Session
from services.db import Base, engine, SessionLocal
from models.item import Item
from models.seed_data import SEED_DATA
from controllers.routers import items as items_router
from routers import api as api_router

app = FastAPI(title="Mi primera API en Python my bro")
@app.on_event("startup")
def on_sartup():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        if(db.query(Item)).count() == 0: 
            now = datetime.utcnow()
            for k, v in SEED_DATA.items():
                db.add(Item(
                    id=k,
                    title=v.get("nombre", "Sin título"),  # Default to 'Sin título' if 'nombre' is missing
                    description=v.get("description", ""),
                    price=v.get("precio", 0),
                    created_at=now
                ))
            db.commit()
app.include_router(items_router.router)
app.include_router(api_router.router, prefix="/api")
@app.get("/")
def root():
        return {"status":"Mi api evaluación 1","docs":"/docs"}