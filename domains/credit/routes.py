from fastapi import APIRouter, Depends, HTTPException
from .models import Credit
from .repository import CreditRepository

from db import SessionDep
from domains.rater.services import calculate_rater_totals
from domains.rater.repository import RaterRepository

# Entry point for Credit Enpoint
router = APIRouter(prefix="/rater/{rater_id}/credit", tags=["Credit"])

# Create Rater
@router.post("/")
def create_creditsure(rater_id:int, credit_data: dict,db: SessionDep):
    # print("Create Credit")
    credit_repo = CreditRepository(db)
    rater = RaterRepository(db).find_by_id(rater_id)
    credit = Credit(**credit_data)
    saved_credit = credit_repo.save(credit)
    calculate_rater_totals(rater)
    db.commit()
    return {"message": "Credit created", "creditsure_id": saved_credit.id}
    return {"message","Credit Created"}


@router.get("/")
def get_credit_by_rater_id(rater_id: int, db: SessionDep):
    credit_repo = CreditRepository(db)
    credit_repo.find_all()
    return {"message":"nice"}

@router.delete("/{credit_id}")
def delete_credit(rater_id: int, credit_id: int,db: SessionDep):
    # """Delete an item by ID."""
    credit_repo = CreditRepository(db)
    rater = RaterRepository(db).find_by_id(rater_id)
    success = credit_repo.delete_credit(credit_id)
    calculate_rater_totals(rater)
    db.commit()
    if not success:
        raise HTTPException(status_code=404, detail="Cart not found")

    return {"message": "Item deleted"}
