from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from domains.rater.models import Rater
from datetime import datetime

class Credit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str= Field(default=None,nullable=True)
    description: str= Field(default=None,nullable=True)
    note: str= Field(default=None,nullable=True)
    factor: float= Field(default=None,nullable=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Define relationship to parent Rater
    rater_id: int = Field(foreign_key="rater.id", index=True)
    rater: Optional[Rater] = Relationship(back_populates="credits")

    def update_timestamp(self):
        self.updated_at = datetime.utcnow()