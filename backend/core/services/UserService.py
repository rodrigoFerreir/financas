
from email.policy import default
from serializers.UserSerializer import UserIn
from repositories.UserRepository import (
    list_user_from_id,
    save_user, 
    list_user_from_email, 
    update_user,
    list_all_users,
    delete_user)


async def create_new_user(user: UserIn):
    try:
        user_listed = await list_user_from_email(user.email)
        
        if user_listed:
            return {
                "msg": f"Email {user.email}, já cadastrado",
                "dados": "",
                "status": 400
            }
        else:
            new_user = await save_user(user)
            return {
                "msg": "Usuário cadastrado com sucesso!",
                "dados": new_user,
                "status": 201
            }

    except Exception as error:
        return  {
            "msg": "Erro interno no servidor!",
            "dados": str(error),
            "status": 500
        }


async def list_from_id(id:str) -> dict:
    try:
        user = await list_user_from_id(id=id)
        
        if user:
             return {
                "msg": f" Usuarios logado",
                "dados": user,
                "status": 200
            }
        else:
             return {
                "msg": f"Nenhum usuario cadastrado",
                "dados": "",
                "status": 404
            }    
    except Exception as error:
        return  {
            "msg": "Erro interno no servidor!",
            "dados": str(error),
            "status": 500
        }
