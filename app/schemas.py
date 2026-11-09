from datetime import datetime

from pydantic import BaseModel, Field


class SkuIn(BaseModel):
    sku: str = Field(min_length=1, max_length=120)
    title: str
    quantity: str
    status: str = "in_stock"


class SkuOut(SkuIn):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
