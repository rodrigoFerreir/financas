from models.AccountModel import AccountModel
from repositories.AccountRepository import (save_account, list_all_accounts, list_account_from_id)


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

async def get_all_account():
    try:
        accounts = await list_all_accounts()
        return {
            "msg": "Lançamentos encontrados com sucesso!",
            "dados": accounts,
            "status": 200
        }

    except Exception as error:
        return  {
            "msg": "Erro interno no servidor!",
            "dados": str(error),
            "status": 500
        }

async def get_account_by_id(id:str):
    try:
        account = await list_account_from_id(id=id)
        if account:
             return {
                "msg": f"Lançamento encontrado",
                "dados": account,
                "status": 200
            }
        else:
             return {
                "msg": f"Nenhum lançamento encontrado",
                "dados": "",
                "status": 404
            }    
    except Exception as error:
        return  {
            "msg": "Erro interno no servidor!",
            "dados": str(error),
            "status": 500
        }
