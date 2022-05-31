from models.AccountModel import AccountModel
from repositories.AccountRepository import (save_account)


async def create_new_account(account: AccountModel):
    try:
        new_account = await save_account(account)
        return {
            "msg": "Conta cadastrada com sucesso!",
            "dados": new_account,
            "status": 201
        }

    except Exception as error:
        return  {
            "msg": "Erro interno no servidor!",
            "dados": str(error),
            "status": 500
        }
