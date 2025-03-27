from enum import Enum
from uuid import UUID
from pydantic import BaseModel


class CategoryType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"
    INVESTMENT = "investment"
    TRANSFER = "transfer"


class Category(BaseModel):
    id: UUID
    name: str
    type: CategoryType
    description: str = ""
    
    class Config:
        orm_mode = True