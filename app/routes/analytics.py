from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product_view_event import ProductViewEvent
from app.models.enquiry_click_event import EnquiryClickEvent

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.post("/product-view/{product_id}")
def log_product_view(product_id: int, db: Session = Depends(get_db)):
    event = ProductViewEvent(product_id=product_id)
    db.add(event)
    db.commit()
    return {"status": "view_logged"}

@router.post("/enquiry-click/{product_id}")
def log_enquiry_click(
    product_id: int,
    quantity: int | None = None,
    option_selected: str | None = None,
    db: Session = Depends(get_db)
):
    event = EnquiryClickEvent(
        product_id=product_id,
        quantity=quantity,
        option_selected=option_selected
    )
    db.add(event)
    db.commit()
    return {"status": "enquiry_logged"}

