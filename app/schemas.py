from pydantic import BaseModel
from datetime import datetime

class InventoryBase(BaseModel):
    name: str
    category: str
    quantity: int
    price: float
    status: str

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(InventoryBase):
    pass

class InventoryResponse(InventoryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True