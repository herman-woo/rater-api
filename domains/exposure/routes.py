from fastapi import APIRouter, Depends, HTTPException
from .models import Exposure
from .repository import ExposureRepository

from db import SessionDep
from domains.rater.services import calculate_rater_totals
from domains.rater.repository import RaterRepository

# Entry point for Exposure Enpoint
router = APIRouter(prefix="/rater/{rater_id}/exposure", tags=["Exposure"])

# Create Rater
@router.post("/")
def create_exposure(rater_id:int, expo_data: dict,db: SessionDep):
    expo_repo = ExposureRepository(db)
    rater = RaterRepository(db).find_by_id(rater_id)
    expo = Exposure(**expo_data)
    saved_expo = expo_repo.save(expo)
    calculate_rater_totals(rater)
    db.commit()
    return {"message": "Exposure created", "exposure_id": saved_expo.id}


@router.get("/")
def get_exposures_by_rater_id(rater_id: int, db: SessionDep):
    expo_repo = ExposureRepository(db)
    expo_repo.find_all()
    return {"message":"nice"}

@router.delete("/{expo_id}")
def delete_cart(rater_id: int, expo_id: int,db: SessionDep):
    # """Delete an item by ID."""
    expo_repo = ExposureRepository(db)
    rater = RaterRepository(db).find_by_id(rater_id)
    success = expo_repo.delete_exposure(expo_id)
    calculate_rater_totals(rater)
    db.commit()
    if not success:
        raise HTTPException(status_code=404, detail="Cart not found")

    return {"message": "Item deleted"}
