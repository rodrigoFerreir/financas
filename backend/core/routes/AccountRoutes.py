
from fastapi import APIRouter, Body, HTTPException, Depends, Header
from serializers.AccountSerializer import AccountIn
from services.AccountService import (create_new_account)

router = APIRouter()


@router.post('/create', response_description="Rota para criar um novo Lançamento")
async def new_account(account: AccountIn = Body(...)):
    try:
        result_account = await create_new_account(account)

        if not result_account["status"] == 201:
            raise HTTPException(status_code=result_account["status"], detail=result_account["msg"])

        return result_account
        
    except Exception as error:
        raise HTTPException(status_code=500)
