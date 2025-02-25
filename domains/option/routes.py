from fastapi import APIRouter, Depends, HTTPException
from .models import Option
from .repository import OptionRepository

from db import SessionDep
from domains.rater.services import calculate_rater_totals
from domains.rater.repository import RaterRepository

# Entry point for Credit Enpoint
router = APIRouter(prefix="/rater/{rater_id}/option", tags=["Options"])

# Create Rater
@router.post("/")
def create_option(rater_id:int, credit_data: dict,db: SessionDep):
    option_repo = OptionRepository(db)
    rater = RaterRepository(db).find_by_id(rater_id)
    option = Option(**credit_data)
    saved_option = option_repo.save(option)
    # # calculate_rater_totals(rater)
    db.commit()
    return {"message": "Option created", "option_id": saved_option.id}
    # return {"message": "Option Created"}


@router.get("/")
def get_option_by_rater_id(rater_id: int, db: SessionDep):
    option_repo = OptionRepository(db)
    option_repo.find_all()
    return {"message":"found options"}

@router.delete("/{option_id}")
def delete_option(rater_id: int, option_id: int,db: SessionDep):
    option_repo = OptionRepository(db)
    rater = RaterRepository(db).find_by_id(rater_id)
    success = option_repo.delete_option(option_id)
    # calculate_rater_totals(rater)
    db.commit()
    if not success:
        raise HTTPException(status_code=404, detail="Cart not found")

    return {"message": "Item deleted"}
