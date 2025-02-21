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