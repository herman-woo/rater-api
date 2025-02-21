# from sqlalchemy.orm import Session
# from .models import Rater, Exposure
# import math

# Calculate totals based on current values
# def calculate_rater_totals(rater: Rater):
    # subtotal = sum(item.premium for item in rater.items)
    # tax_factor = math.prod(tax.factor for tax in rater.taxes) if rater.taxes else 1.0
    # final_total = subtotal * tax_factor

    # rater.subtotal = subtotal
    # rater.taxes_total = tax_factor
    # rater.final_total = final_total

    # return rater

# A calculation that goes through all items
# def recalculate_rater_totals(rater: Rater):
#     subtotal = sum(item.premium for item in rater.items)

#     tax_factor = math.prod(tax.factor for tax in rater.taxes) if rater.taxes else 1.0

#     final_total = subtotal * tax_factor

#     rater.subtotal = subtotal
#     rater.taxes_total = tax_factor
#     rater.final_total = final_total

#     return rater

# def add_item_to_rater(db: Session, rater_id: int, item_data: dict):
#     """ Adds an item to the rater and updates totals. """
#     rater = db.get(Rater, rater_id)
#     if not rater:
#         raise ValueError("rater not found.")

#     new_item = Exposure(rater_id=rater_id, **item_data)
#     db.add(new_item)
#     db.commit()
#     db.refresh(rater)

#     # Recalculate totals
#     updated_rater = calculate_rater_totals(rater)
#     db.commit()
    
#     return updated_rater
