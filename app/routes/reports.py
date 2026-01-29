from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.deps import get_db
from app.models import InventoryItem

router = APIRouter(prefix="/api/reports", tags=["Reports"])

@router.get("/summary")
def inventory_summary(db: Session = Depends(get_db)):
    total = db.query(func.count(InventoryItem.id)).scalar()
    in_stock = db.query(func.count()).filter(InventoryItem.status == "In Stock").scalar()
    low_stock = db.query(func.count()).filter(InventoryItem.status == "Low Stock").scalar()
    out_of_stock = db.query(func.count()).filter(InventoryItem.status == "Out of Stock").scalar()

    return {
        "total_items": total,
        "in_stock": in_stock,
        "low_stock": low_stock,
        "out_of_stock": out_of_stock
    }