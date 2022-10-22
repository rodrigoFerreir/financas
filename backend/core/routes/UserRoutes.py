from fastapi import APIRouter, Body, HTTPException, Depends, Header
from middlewares.AuthMiddleware import AuthMiddleware
from serializers.UserSerializer import UserIn, UserOut
from services.UserService import UserService
from services.AuthService import AuthService

router = APIRouter()
user_service = UserService()
auth_service = AuthService()
middleware = AuthMiddleware()


@router.post("/create", response_description="Rota para criar um novo Usuario")
async def new_user(user: UserIn = Body(...)):
    result_user = await user_service.create_new_user(user)

    if not result_user["status"] == 201:
        raise HTTPException(
            status_code=result_user["status"], detail=result_user["msg"]
        )

    return result_user


@router.get(
    "/me",
    response_description="Rota para buscar um Usuario logado",
    dependencies=[Depends(middleware.verify_token)],
)
async def get_info_user_logged(Authorization: str = Header(default="")):
    try:
        token = Authorization.split(" ")[1]
        payload = auth_service.decode_jwt_token(token)

        user = await user_service.list_from_id(id=payload["user_id"])
        if not user["status"] == 200:
            raise HTTPException(status_code=user["status"], detail=user["msg"])
        return user

    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail="Erro interno no servidor")
