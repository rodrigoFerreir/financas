from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

from decouple import config
from utils.AuthUtil import generate_hash_password
from models import UserModel


MONGO_DB_URL = config("MONGO_DB_URL")


client_db = AsyncIOMotorClient(MONGO_DB_URL)


database = client_db.financas

user_collection = database.get_collection("user")


def user_helper(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "name": str(user["name"]),
        "email": str(user["email"]),
        "password": str(user["password"]),
        "avatar": str(user["avatar"]),
    }


async def save_user(user: UserModel) -> dict:
    user.password = generate_hash_password(user.password)
    new_user = await user_collection.insert_one(user.__dict__)

    get_new_user = await user_collection.find_one({"_id": new_user.inserted_id})

    return user_helper(get_new_user)


async def list_all_users():
    users = await user_collection.find()
    return users


async def list_user_from_id(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})

    if user:
        return user_helper(user)
    else:
        return None


async def list_user_from_email(email: str) -> dict:
    user = await user_collection.find_one({"email": email})
    if user:
        return user_helper(user)
    else:
        return None


async def update_user(id: str, data_update: dict):
    user = await user_collection.find_one({"_id": ObjectId(id)})

    if user:
        update_user = await user_collection.update_one(
            {{"_id": ObjectId(id)}, {"$set": data_update}}
        )

        return user_helper(update_user)


async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})

    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
