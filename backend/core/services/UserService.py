from serializers.UserSerializer import UserIn
from repositories.UserRepository import UserRepository


class UserService:
    user_repository = UserRepository()

    async def create_new_user(self, user: UserIn):
        try:
            user_listed = await self.user_repository.list_user_from_email(
                email=user.email
            )

            if user_listed:
                return {
                    "msg": f"Email {user.email}, já cadastrado",
                    "dados": "",
                    "status": 400,
                }
            else:
                new_user = await self.user_repository.save_user(user)
                return {
                    "msg": "Usuário cadastrado com sucesso!",
                    "dados": new_user,
                    "status": 201,
                }

        except Exception as error:
            return {
                "msg": "Erro interno no servidor!",
                "dados": str(error),
                "status": 500,
            }

    async def list_from_id(self, id: str) -> dict:
        try:
            user = await self.user_repository.list_user_from_id(id=id)

            if user:
                return {"msg": f" Usuarios logado", "dados": user, "status": 200}
            else:
                return {"msg": f"Nenhum usuario cadastrado", "dados": "", "status": 404}
        except Exception as error:
            return {
                "msg": "Erro interno no servidor!",
                "dados": str(error),
                "status": 500,
            }
