from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from decimal import Decimal
from datetime import datetime
from domains.rater.models import Rater

class Option(SQLModel, table=True):
    __tablename__ = "quote_options"

    id: Optional[int] = Field(default=None, primary_key=True)
    per_limit: float = Field(default=Decimal(0))
    total_limit: float = Field(default=Decimal(0))
    retention: float = Field(default=Decimal(0))
    terms: int = Field(default=1)
    total_premium: float = Field(default=Decimal(0))
    final_premium: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    rater_id: int = Field(foreign_key="rater.id", index=True)
    rater: Optional[Rater] = Relationship(back_populates="options")

    def update_timestamp(self):
        self.updated_at = datetime.utcnow()