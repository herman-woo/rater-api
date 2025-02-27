from fastapi import APIRouter
from .naics_codes import naics_with_premiums
from .quantitative_credits import cover_modification_factors

router = APIRouter()

@router.get("/codes")
async def get_naics_codes():
    """Returns the full NAICS codes with premiums."""
    return naics_with_premiums

@router.get("/codes/{code}")
async def get_naics_code_detail(code: int):
    """Returns details for a specific NAICS code."""
    return naics_with_premiums.get(code, {"description": "Unknown", "premium": 0})

# @router.get("/mods/{code}")
# async def get_naics_code_detail(code: int):
#     """Returns details for a specific NAICS code."""
#     return naics_with_premiums.get(code, {"description": "Unknown", "premium": 0})

@router.get("/mods/quantitative")
async def get_cover_mods():
    print("herfbnxfghgfdjhfg  ")
    """Returns the full cover mod descriptions with factors."""
    """sdfsdfsdf"""
    return cover_modification_factors