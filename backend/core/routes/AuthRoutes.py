from fastapi import APIRouter, Body, HTTPException
from services.AuthService import AuthService
from serializers.UserSerializer import UserLogin

router = APIRouter()
auth_service = AuthService()


@router.post("/login")
async def auth(user: UserLogin = Body(...)):
    try:
        response = await auth_service.login_service(user)

        if not response["status"] == 200:
            raise HTTPException(status_code=response["status"], detail=response["msg"])

        del response["dados"]["password"]
        token = auth_service.create_jwt_token(user_id=response["dados"]["_id"])

        response["token"] = token

        return response
    except Exception as err:
        raise HTTPException(
            status_code=response["status"], detail="Erro interno no servidor"
        )
