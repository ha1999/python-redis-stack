from redis_om import (Field, JsonModel)
from pydantic import PositiveInt
from typing import List

from models.address import Address

class Person(JsonModel):
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    age: PositiveInt = Field(index=True)
    address: Address
    skills: List[str] = Field(index=True)
    personal_statement: str = Field(index=True, full_text_search=True)