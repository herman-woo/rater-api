from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from .models import Credit
from db import engine

#Repository Module for Accesing SQL database
class CreditRepository:
    def __init__(self, session: Session):
        self.session = session

    # CREATE and UPDATE Rater(s)
    def save(self, credit: Credit):
        self.session.add(credit)
        self.session.commit()
        self.session.refresh(credit)
        return credit
    
    
    # READ all
    def find_all(self):
        return self.session.exec(select(Credit)).all()
    
    # READ one
    def find_credit_by_id(self, credit_id: int) -> Credit | None:
        credit = self.session.exec(select(Credit).where(Credit.id == credit_id)).first()
        return credit

    # DELETE one
    def delete_credit(self, credit_id: int):
        credit = self.find_credit_by_id(credit_id)
        if credit:
            self.session.delete(credit)
            self.session.commit()
            return True
        return False