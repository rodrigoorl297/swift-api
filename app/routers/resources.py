from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.db import get_db
from app.models import Sku
from app.schemas import SkuIn, SkuOut

router = APIRouter(prefix="/skus", tags=["skus"])


@router.get("", response_model=list[SkuOut])
def list_items(db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    return db.query(Sku).order_by(Sku.id.desc()).all()


@router.post("", response_model=SkuOut, status_code=status.HTTP_201_CREATED)
def create_item(body: SkuIn, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = Sku(**body.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/{item_id}", response_model=SkuOut)
def get_item(item_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = db.get(Sku, item_id)
    if not row:
        raise HTTPException(status_code=404, detail="not found")
    return row
