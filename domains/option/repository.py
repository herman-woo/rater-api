from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from .models import Option
from db import engine

#Repository Module for Accesing SQL database
class OptionRepository:
    def __init__(self, session: Session):
        self.session = session

    # CREATE and UPDATE Rater(s)
    def save(self, option: Option):
        self.session.add(option)
        self.session.commit()
        self.session.refresh(option)
        return option
    
    def find_all(self):
        return self.session.exec(select(Option)).all()
    
    def find_option_by_id(self, option_id: int) -> Option | None:
        option = self.session.exec(select(Option).where(Option.id == option_id)).first()
        return option

    def delete_option(self, option_id: int):
        option = self.find_option_by_id(option_id)
        if option:
            self.session.delete(option)
            self.session.commit()
            return True
        return False