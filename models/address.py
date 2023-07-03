from redis_om import (EmbeddedJsonModel, Field)
from pydantic import PositiveInt
from typing import Optional

class Address(EmbeddedJsonModel):
    street_number: PositiveInt = Field(index=True)
    unit: Optional[str] = Field(index=False)
    street_name: str = Field(index=True)
    city: str = Field(index=True)
    state: str = Field(index=True)
    postal_code: str = Field(index=True)
    country: str = Field(index=True, default="United Kingdom")