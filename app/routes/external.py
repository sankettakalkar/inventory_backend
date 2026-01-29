import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.deps import get_db
from app.models import InventoryItem

router = APIRouter(prefix="/api/external", tags=["External API"])

@router.get("/convert")
def convert_inventory_value(currency: str = "USD", db: Session = Depends(get_db)):
    total_value = db.query(func.sum(InventoryItem.price * InventoryItem.quantity)).scalar() or 0

    response = requests.get(f"https://api.exchangerate.host/convert", params={
        "from": "INR",
        "to": currency,
        "amount": float(total_value)
    })

    data = response.json()

    return {
        "currency": currency,
        "converted_value": data.get("result")
    }