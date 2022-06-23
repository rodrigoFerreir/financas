from fastapi import APIRouter, Body, HTTPException, Depends, Header
from serializers.AccountSerializer import AccountIn, AccountUpdate
from middlewares.AuthMiddleware import verify_token
from services.AccountService import (
    create_new_account,
    get_all_account,
    get_account_by_id,
    update_account_by_id,
    delete_account_by_id,
)

router = APIRouter()


@router.post(
    "/create",
    response_description="Rota para criar um novo Lançamento",
    dependencies=[Depends(verify_token)],
)
async def new_account(account: AccountIn = Body(...)):
    try:
        result_account = await create_new_account(account)

        if not result_account["status"] == 201:
            raise HTTPException(
                status_code=result_account["status"], detail=result_account["msg"]
            )

        return result_account

    except Exception as error:
        raise HTTPException(status_code=500)


@router.get(
    "/list",
    response_description="Rota para listar todos os Lançamento",
    dependencies=[Depends(verify_token)],
)
async def get_accounts():
    try:
        result_accounts = await get_all_account()
        if not result_accounts["status"] == 200:
            raise HTTPException(
                status_code=result_accounts["status"], detail=result_accounts["msg"]
            )

        return result_accounts

    except Exception as error:
        print(error)
        raise HTTPException(status_code=500)


@router.get(
    "/details/{account_id}",
    response_description="Rota para listar detalhes de um Lançamento",
    dependencies=[Depends(verify_token)],
)
async def get_account(account_id: str):
    try:
        result_account = await get_account_by_id(id=account_id)

        if not result_account["status"] == 200:
            raise HTTPException(
                status_code=result_account["status"], detail=result_account["msg"]
            )

        return result_account

    except Exception as error:
        print(error)
        raise HTTPException(status_code=500)


@router.put(
    "/update/{account_id}",
    response_description="Rota para atualizar dados de um Lançamento",
    dependencies=[Depends(verify_token)],
)
async def updated_account(account_id: str, account: AccountUpdate = Body(...)):
    try:
        result_account = await update_account_by_id(id=account_id, account=account)

        if not result_account["status"] == 200:
            raise HTTPException(
                status_code=result_account["status"], detail=result_account["msg"]
            )

        return result_account

    except Exception as error:
        print(error)
        raise HTTPException(status_code=500)


@router.delete(
    "/delete/{account_id}",
    response_description="Rota para deletar dados de um Lançamento",
    dependencies=[Depends(verify_token)],
)
async def deleted_account(account_id: str):
    try:
        result_account = await delete_account_by_id(id=account_id)

        if not result_account["status"] == 200:
            raise HTTPException(
                status_code=result_account["status"], detail=result_account["msg"]
            )

        return result_account

    except Exception as error:
        print(error)
        raise HTTPException(status_code=500)
