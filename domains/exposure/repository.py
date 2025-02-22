from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from .models import Exposure
from db import engine

#Repository Module for Accesing SQL database
class ExposureRepository:
    def __init__(self, session: Session):
        self.session = session

    # CREATE and UPDATE Rater(s)
    def save(self, exposure: Exposure):
        self.session.add(exposure)
        self.session.commit()
        self.session.refresh(exposure)
        return exposure
    
    def find_all(self):
        return self.session.exec(select(Exposure)).all()
    
    def find_expo_by_id(self, expo_id: int) -> Exposure | None:
        expo = self.session.exec(select(Exposure).where(Exposure.id == expo_id)).first()
        return expo

    def delete_exposure(self, expo_id: int):
        """Delete a item by ID."""
        expo = self.find_expo_by_id(expo_id)
        if expo:
            self.session.delete(expo)
            self.session.commit()
            return True
        return False