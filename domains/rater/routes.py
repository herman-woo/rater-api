from fastapi import APIRouter, Depends, HTTPException
from .models import Rater
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
    return {"message": "Rater created", "id": saved_rater.id}

#Get all Raters, without children
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

    result = rater.model_dump()
    result["items"] = [exposure.model_dump() for exposure in rater.exposures]
    result["mods"] = [credit.model_dump() for credit in rater.credits]
    result["options"] = [option.model_dump() for option in rater.options]
    return result

@router.get("/account/{account_id}")
def get_rater_by_account_id(account_id: int, db: SessionDep):
    rater_repo = RaterRepository(db)
    rater = rater_repo.find_by_id_account_id(account_id)

    if not rater:
        raise HTTPException(status_code=404, detail="rater not found")

    result = rater.model_dump()
    result["items"] = [exposure.model_dump() for exposure in rater.exposures]
    result["mods"] = [credit.model_dump() for credit in rater.credits]
    result["options"] = [option.model_dump() for option in rater.options]
    return result

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