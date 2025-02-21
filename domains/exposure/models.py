from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from domains.rater.models import Rater


class Exposure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    note: str = Field(default=None,nullable=True)
    modifier: float = Field(default=None,nullable=True)
    quantity: int = Field(default=None,nullable=True)
    premium: float = Field(default=None,nullable=True)
    product_description: str = Field(default=None,nullable=True)
    naics_code: int = Field(default=None,nullable=True)
    naics_premium: float = Field(default=None,nullable=True)

    # Define relationship to parent Rater
    rater_id: int = Field(foreign_key="rater.id", index=True)  # Foreign key linking to Cart
    rater: Optional[Rater] = Relationship(back_populates="exposures")