from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import InventoryItem
from app.schemas import InventoryCreate, InventoryUpdate, InventoryResponse
from app.core.deps import get_db

router = APIRouter(
    prefix="/api/items",
    tags=["Inventory"]
)

# ------------------------
# CREATE
# ------------------------
@router.post("")
@router.post("/")
def create_item(
    item: InventoryCreate,
    db: Session = Depends(get_db)
):
    db_item = InventoryItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# ------------------------
# READ ALL
# ------------------------
@router.get("")
@router.get("/")
def list_items(db: Session = Depends(get_db)):
    return db.query(InventoryItem).all()


# ------------------------
# READ ONE
# ------------------------
@router.get("/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# ------------------------
# UPDATE
# ------------------------
@router.put("/{item_id}")
def update_item(
    item_id: int,
    data: InventoryUpdate,
    db: Session = Depends(get_db)
):
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in data.dict().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


# ------------------------
# DELETE
# ------------------------
@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}