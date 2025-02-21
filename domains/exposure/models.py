from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Exposure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # Define relationship to parent Rater
    rater_id: int = Field(foreign_key="rater.id", index=True)  # Foreign key linking to Cart
    rater: Optional["Rater"] = Relationship(back_populates="exposures")
    # note: str = Field(default=None)
    # modifier: float = Field(default=None)
    # quantity: int = Field(default=None)
    # premium: float = Field(default=None)
    # product_description: str = Field(default=None)
    # naics_code: int = Field(default=None)
    # naics_premium: float = Field(default=None)
