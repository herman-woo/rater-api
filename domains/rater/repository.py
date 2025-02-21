from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload
from .models import Rater

#Repository Module for Accesing SQL database
class RaterRepository:
    def __init__(self, session: Session):
        self.session = session

    # CREATE and UPDATE Rater(s)
    def save(self, rater: Rater):
        self.session.add(rater)
        self.session.commit()
        self.session.refresh(rater)
        return rater
    
    # GET/Retrieve All Raters
    def find_all(self):
        return self.session.exec(select(Rater)).all()
    
    # GET Rater by it's own ID
    def find_by_id(self, rater_id: int) -> Rater | None:
        rater = self.session.exec(
            select(Rater)
            .where(Rater.id == rater_id)
            .options(joinedload(Rater.exposures)) 
        ).first()
        print("DEBUG: Rater retrieved:", rater)
#         print("DEBUG: Cart items:", rater.items if cart else "No cart found")
        return rater
    

    # def get_rater_by_id(self, rater_id: int):
    # stmt = (
    #     select(Rater)
    #     .where(Rater.id == rater_id)
    #     .options(joinedload(Rater.children))  # Replace 'children' with your actual relationship
    # )
    # result = self.session.exec(stmt).first()  # Ensure only one result is fetched
    # return result  # Now it includes nested children
    
    # Delete a Rater by ID
    def delete(self, rater_id: int):
        rater = self.find_by_id(rater_id)
        if rater:
            self.session.delete(rater)
            self.session.commit()
            return True
        return False
    














    

#     # def get_items_by_cart_id(self, cart_id: int) -> list[Exposure]:
#     #     """Retrieve all CartItems for a specific cart_id."""
#     #     return self.session.exec(
#     #         select(Exposure).where(Exposure.cart_id == cart_id)
#     #     ).all()

    
    

# #     def find_item_by_id(self, item_id: int) -> Exposure | None:
# #         item = self.session.exec(select(Exposure).where(Exposure.id == item_id)).first()
# #         return item
    
# #     def delete_item(self, item_id: int):
# #         """Delete a item by ID."""
# #         item = self.find_item_by_id(item_id)
# #         if item:
# #             self.session.delete(item)
# #             self.session.commit()
# #             return True
# #         return False
    
# #     def find_mod_by_id(self, mod_id: int) -> Modifier | None:
# #         mod = self.session.exec(select(Modifier).where(Modifier.id == mod_id)).first()
# #         print(mod)
# #         return mod    
# #     def delete_mod(self, mod_id: int):
# #         """Delete a item by ID."""
# #         print("Delete Mod")
# #         mod = self.find_mod_by_id(mod_id)
# #         if mod:
# #             self.session.delete(mod)
# #             self.session.commit()
# #             return True
# #         return False    