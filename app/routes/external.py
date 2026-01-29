from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from decimal import Decimal
import requests

from app.models import InventoryItem
from app.core.deps import get_db

router = APIRouter(
    prefix="/api/external",
    tags=["External APIs"]
)

@router.get("/convert")
def convert_currency(currency: str, db: Session = Depends(get_db)):
    # 1. Calculate total inventory value (INR)
    total_value = (
        db.query(func.sum(InventoryItem.price * InventoryItem.quantity))
        .scalar()
        or Decimal("0")
    )

    if total_value == 0:
        return {
            "currency": currency,
            "converted_value": 0
        }

    # 2. Fetch exchange rates (FREE API, no key)
    response = requests.get(
        "https://api.exchangerate-api.com/v4/latest/INR",
        timeout=10
    )
    data = response.json()

    rate = data.get("rates", {}).get(currency)

    if rate is None:
        return {
            "currency": currency,
            "converted_value": 0
        }

    # 3. Convert safely (Decimal * Decimal)
    converted_value = total_value * Decimal(str(rate))

    return {
        "currency": currency,
        "converted_value": round(converted_value, 2)
    }