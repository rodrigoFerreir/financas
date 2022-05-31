from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

from decouple import config
from utils.AuthUtil import generate_hash_password
from models import AccountModel


MONGO_DB_URL = config('MONGO_DB_URL')


client_db = AsyncIOMotorClient(MONGO_DB_URL)


database = client_db.financas

account_collection = database.get_collection('user')


def account_helper(account) -> dict:
   return {
       "_id":str(account["_id"]),
       "name":str(account["name"]),
       "email":str(account["email"]),
       "password":str(account["password"]),
       "avatar":str(account["avatar"]),
   } 

async def save_account(account: AccountModel)-> dict:
    account.password = generate_hash_password(account.password)
    new_account = await account_collection.insert_one(account.__dict__)

    get_new_account =  await account_collection.find_one({"_id":new_account.inserted_id})

    return account_helper(get_new_account)


async def list_all_accounts():
    accounts = await account_collection.find()
    return accounts


async def list_account_from_email(email:str) -> dict:
    account = await account_collection.find_one({"email":email})
    if account:
        return account_helper(account)
    else:
        return None


async def update_account(id: str, data_update: dict):
    account = await account_collection.find_one({"_id": ObjectId(id)})

    if account:
        update_account = await account_collection.update_one({
            {"_id": ObjectId(id)}, {"$set": data_update}
        })

        return account_helper(update_account)


async def delete_user(id:str):
    user = await account_collection.find_one({"_id": ObjectId(id)})

    if user:
        await account_collection.delete_one({"_id": ObjectId(id)})
