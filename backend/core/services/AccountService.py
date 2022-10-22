from models.UserModel import UserModel
from serializers.AccountSerializer import AccountIn
from repositories.AccountRepository import AccountRepository


class AccountService:
    account_repository = AccountRepository()

    async def create_new_account(self, account: AccountIn, user:str):
        try:
            new_account = await self.account_repository.save_account(account, user)
            return {
                "msg": "Conta cadastrada com sucesso!",
                "dados": new_account,
                "status": 201,
            }

        except Exception as error:
            return {
                "msg": "Erro interno no servidor!",
                "dados": str(error),
                "status": 500,
            }

    async def get_all_account(self):
        try:
            accounts = await self.account_repository.list_all_accounts()
            return {
                "msg": "Lançamentos encontrados com sucesso!",
                "dados": accounts,
                "status": 200,
            }

        except Exception as error:
            return {
                "msg": "Erro interno no servidor!",
                "dados": str(error),
                "status": 500,
            }

    async def get_account_by_id(self, id: str):
        try:
            account = await self.account_repository.list_account_from_id(id=id)
            if account:
                return {
                    "msg": f"Lançamento encontrado",
                    "dados": account,
                    "status": 200,
                }
            else:
                return {
                    "msg": f"Nenhum lançamento encontrado",
                    "dados": "",
                    "status": 404,
                }
        except Exception as error:
            return {
                "msg": "Erro interno no servidor!",
                "dados": str(error),
                "status": 500,
            }

    async def update_account_by_id(self, id: str, account: AccountIn):
        try:
            account = await self.account_repository.update_account(
                id=id, data_update=account
            )
            if account:
                return {
                    "msg": f"Lançamento atualizado",
                    "dados": account,
                    "status": 200,
                }
            else:
                return {
                    "msg": f"Nenhum lançamento encontrado",
                    "dados": "",
                    "status": 404,
                }
        except Exception as error:
            return {
                "msg": "Erro interno no servidor!",
                "dados": str(error),
                "status": 500,
            }

    async def delete_account_by_id(self, id: str):
        try:
            account = await self.account_repository.delete_account(id=id)
            if account:
                return {
                    "msg": f"Lançamento deletado",
                    "dados": True,
                    "status": 200,
                }
            else:
                return {
                    "msg": f"Nenhum lançamento encontrado",
                    "dados": False,
                    "status": 404,
                }
        except Exception as error:
            return {
                "msg": "Erro interno no servidor!",
                "dados": str(error),
                "status": 500,
            }
