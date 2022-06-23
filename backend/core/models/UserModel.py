from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    """
    Classe que reprensenta um usuario
    """

    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    avatar: str = Field(...)
    create_at: datetime = Field(default_factory=datetime.now)

    class Config:

        schema_extra = {
            "user": {
                "name": "Teste",
                "email": "teste@exemple.com",
                "password": "dajskdj.fsajfsa0qwdksa",
                "avatar": "image.png",
                "create_at": "dd-mm-YY",
            }
        }
