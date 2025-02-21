from fastapi import APIRouter, Depends, HTTPException
from .models import Exposure
from .repository import ExposureRepository
from db import SessionDep

# Entry point for Exposure Enpoint
router = APIRouter(prefix="/rater/{rater_id}/exposure", tags=["Exposure"])

# Create Rater
@router.post("/")
def create_exposure(expo_data: dict,db: SessionDep):
    print("Exposure Create:")
    expo_repo = ExposureRepository(db)
    expo = Exposure(**expo_data)
    saved_expo = expo_repo.save(expo)
    return {"message": "Exposure created", "exposure_id": saved_expo.id}