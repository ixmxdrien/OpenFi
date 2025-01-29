from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class TransactionBase(BaseModel):
    amount: float
    type: TransactionType
    category: Optional[str] = None
    description: Optional[str] = None
    date: datetime = datetime.now()

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: str
    user_id: str

    class Config:
        from_attributes = True