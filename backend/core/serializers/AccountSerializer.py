
from pydantic import BaseModel


class AccountIn(BaseModel):
    title: str
    description: str
    value: float
    category: str
    type_account: str