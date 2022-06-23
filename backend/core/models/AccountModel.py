from datetime import datetime

from pydantic import BaseModel, Field


class AccountModel(BaseModel):
    """
    Classe responsavel pela criação de contas(receitas e despesas dos usuarios)
    """

    title: str = Field(...)
    description: str = Field(...)
    value: float = Field(...)
    category: str = Field(...)
    type_account: str = Field(...)
    create_at: datetime = Field(default_factory=datetime.now)

    class Config:
        schema_extra = {
            "account": {
                "title": "Titulo da conta",
                "description": "exemplo de conta",
                "value": "300.96",
                "category": "Gastos Gerais/Alimentação/Restaurante/Agua/Luz",
                "type_account": "receita/despesa",
                "create_at": "dd-mm-YY",
            }
        }
