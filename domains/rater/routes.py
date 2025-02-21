from fastapi import APIRouter, Depends, HTTPException
from .models import Rater
# from .models import Rater, Exposure, Modifier
# from .services import calculate_cart_totals
from .repository import RaterRepository
from db import SessionDep

# Entry point for Rater Enpoint
router = APIRouter(prefix="", tags=["Rater"])

# Create Rater
@router.post("/")
def create_rater(rater_data: dict,db: SessionDep):
    rater_repo = RaterRepository(db)
    rater = Rater(**rater_data)
    saved_rater = rater_repo.save(rater)
    return {"message": "Rater created", "rater_id": saved_rater.id}

@router.get("/")
def get_all_raters(db: SessionDep):
    rater_repo = RaterRepository(db)
    return rater_repo.find_all()

@router.get("/{rater_id}")
def get_cart(rater_id: int, db: SessionDep):
    rater_repo = RaterRepository(db)
    rater = rater_repo.find_by_id(rater_id)

    if not rater:
        raise HTTPException(status_code=404, detail="rater not found")
    return rater
    # Explicitly convert `Cart` to a dictionary, including `items`
    # return {
        # "id": rater.id,
        # "subtotal_premium": rater.subtotal_premium,  # Convert Decimal to float for JSON compatibility
        # "total_modifiers": float(rater.total_modifiers),
        # "final_premium": float(rater.final_premium),
        # "items": [
        #     {
        #         "id": item.id,
        #         "cart_id": item.cart_id,
        #         "product_description": item.product_description,
        #         "premium": float(item.premium),  # Convert Decimal to float
        #         "quantity": item.quantity,
        #         "naics_premium": float(item.naics_premium),
        #         "note": item.note,
        #         "naics_code": item.naics_code,
        #         "modifier": item.modifier
        #     }
        #     for item in cart.items
        # ],
        # "mods": [
        #     {
        #         "id": mod.id,
        #         "cart_id": mod.cart_id,
        #         "type": mod.type,
        #         "description": mod.description,
        #         "factor": mod.factor,
        #         "note": mod.note
        #     }
        #     for mod in cart.taxes
        # ]
    # }


@router.delete("/{rater_id}")
def delete_cart(rater_id: int, db: SessionDep):
    rater_repo = RaterRepository(db)
    success = rater_repo.delete(rater_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cart not found")
    return {"message": "Cart deleted"}













# @router.post("/{rater_id}/add-item")
# def add_item(rater_id: int, item_data: dict, db: SessionDep):
#     """Add an item to a cart and recalculate totals."""
#     cart_repo = CartRepository(db)
#     cart = cart_repo.find_by_id(rater_id)
#     if not cart:
#         raise HTTPException(status_code=404, detail="Cart not found")

#     # Create CartItem from request data
#     new_item = Exposure(rater_id=rater_id, **item_data)
#     db.add(new_item)
#     db.commit()
#     db.refresh(cart)

#     # Recalculate totals
#     updated_cart = calculate_cart_totals(cart)
#     db.commit()

#     return {"message": "Item added", "cart": updated_cart}


# @router.post("/{cart_id}/add-mod")
# def add_item(cart_id: int, tax_data: dict, db: SessionDep):
#     """Add an item to a cart and recalculate totals."""
#     cart_repo = CartRepository(db)
#     cart = cart_repo.find_by_id(cart_id)
#     if not cart:
#         raise HTTPException(status_code=404, detail="Cart not found")

#     # Create Tax from request data
#     print("HERERER")
#     new_item = Modifier(cart_id=cart_id, **tax_data)
#     db.add(new_item)
#     db.commit()
#     db.refresh(cart)

#     # # Recalculate totals
#     updated_cart = calculate_cart_totals(cart)
#     db.commit()

#     return {"message": "Item added", "cart": updated_cart}
#     # return{"Message":"Tax Added"}


# @router.delete("/delete-item/{cart_id}/{item_id}")
# def delete_cart(cart_id: int, item_id: int,db: SessionDep):
#     # """Delete an item by ID."""
#     cart_repo = CartRepository(db)
#     cart = cart_repo.find_by_id(cart_id)
#     success = cart_repo.delete_item(item_id)
#     updated_cart = calculate_cart_totals(cart)
#     db.commit()
#     if not success:
#         raise HTTPException(status_code=404, detail="Cart not found")

#     return {"message": "Item deleted"}


# @router.get("/{cart_id}/items")
# def get_cart_items(cart_id: int, db: SessionDep):
#     """Retrieve all items in a cart by cart_id."""
#     cart_repo = CartRepository(db)
#     cart_items = cart_repo.get_items_by_cart_id(cart_id)

#     if not cart_items:
#         raise HTTPException(status_code=404, detail="No items found for this cart")

#     return {"cart_id": cart_id, "items": cart_items}

# @router.delete("/delete-mod/{cart_id}/{mod_id}")
# def delete_cart(cart_id: int, mod_id: int,db: SessionDep):
#     # """Delete an item by ID."""
#     cart_repo = CartRepository(db)
#     cart = cart_repo.find_by_id(cart_id)
#     success = cart_repo.delete_mod(mod_id)
#     updated_cart = calculate_cart_totals(cart)
#     db.commit()
#     if not success:
#         raise HTTPException(status_code=404, detail="Cart not found")

#     return {"message": "Mod deleted"}