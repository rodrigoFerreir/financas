from fastapi import APIRouter, Body, HTTPException, Depends, Header
from middlewares.AuthMiddleware import verify_token
from serializers.UserSerializer import UserIn, UserOut
from services.UserService import (create_new_user, list_from_id, list_all_users, update_user, delete_user)
from services.AuthService import decode_jwt_token

router = APIRouter()

@router.post('/create', response_description="Rota para criar um novo Usuario")
async def new_user(user: UserIn = Body(...)):
    result_user = await create_new_user(user)

    if not result_user["status"] == 201:
        raise HTTPException(status_code=result_user["status"], detail=result_user["msg"])

    return result_user


@router.get('/me', response_description="Rota para buscar um Usuario logado", dependencies=[Depends(verify_token)])
async def get_info_user_logged(Authorization: str = Header(default='')):
    try:
        token = Authorization.split(' ')[1]
        payload = decode_jwt_token(token)

        user = await list_from_id(payload['user_id'])

        if not user["status"] == 200:
            raise HTTPException(status_code=user["status"], detail=user["msg"])
        return user
        
    except Exception as error:
        raise HTTPException(status_code=500, detail='Erro interno no servidor')
