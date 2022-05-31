from services.AuthService import create_jwt_token, login_service
from serializers.UserSerializer import UserLogin
from fastapi import APIRouter, Body, HTTPException

router = APIRouter()


@router.post('/login')
async def auth(user: UserLogin = Body(...)):
    response = await login_service(user)
    
    if not response["status"] == 200:
        raise HTTPException(status_code=response["status"], detail=response["msg"])

    del response['dados']['password']
    token = create_jwt_token(response['dados']['_id'])
    
    response['token'] = token
    
    return response
