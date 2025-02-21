from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from decimal import Decimal
from datetime import datetime
# from domains.exposure.models import Exposure

class Rater(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    year: int = Field(default=None,nullable=True)
    business_unit_id: int = Field(default=None,nullable=True)
    business_unit: str = Field(default=None,nullable=True)
    named_insured_id: int = Field(default=None,nullable=True)
    named_insured: str = Field(default=None,nullable=True)
    account_id: int = Field(default=None,nullable=True)
    product_id: int = Field(default=None,nullable=True)
    product: str = Field(default=None,nullable=True)
    subtotal_premium: float = Field(default=Decimal(0))
    total_modifiers: float = Field(default=Decimal(0))
    final_premium: float = Field(default=Decimal(0))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Reverse relationship
    exposures: List["Exposure"] = Relationship(back_populates="rater")#, sa_relationship_kwargs={"lazy": "joined"}*/)


    def update_timestamp(self):
        self.updated_at = datetime.utcnow()