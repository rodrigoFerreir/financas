from datetime import datetime

from pydantic import BaseModel, Field


class AccountPlanningModel(BaseModel):
    """
    Classe que reprensenta o planejamento de contas
    """

    name: str = Field(...)
    descript: str = Field(...)
    type_account_planning: str = Field(...)

    class Config:

        schema_extra = {
            "account_planning": {
                "name": "Teste",
                "descript": "teste",
                "type_account_planning": "dajskdj.fsajfsa0qwdksa",
            }
        }
