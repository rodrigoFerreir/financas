from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

from decouple import config
from models import AccountModel


MONGO_DB_URL = config("MONGO_DB_URL")


client_db = AsyncIOMotorClient(MONGO_DB_URL)


class AccountRepository:
    database = client_db.financas

    account_collection = database.get_collection("account")

    def account_helper(self, account) -> dict:
        return {
            "_id": str(account["_id"]),
            "title": str(account["title"]),
            "description": str(account["description"]),
            "value": float(account["value"]),
            "category": str(account["category"]),
            "type_account": str(account["type_account"]),
        }

    async def save_account(self, account: AccountModel, user_id: str) -> dict:
        account_dict = account.__dict__
        account_dict["user"] = user_id

        new_account = await self.account_collection.insert_one(account_dict.__dict__)

        get_new_account = await self.account_collection.find_one(
            {"_id": new_account.inserted_id}
        )

        return self.account_helper(get_new_account)

    async def list_all_accounts(self):
        accounts = self.account_collection.aggregate(
            [
                {
                    "$lookup": {
                        "from": "user",
                        "localField": "user_id",
                        "foreignField": "_id",
                        "as": "user",
                    }
                }
            ]
        )
        all_accounts = []

        async for account in accounts:
            all_accounts.append(self.account_helper(account))

        return all_accounts

    async def list_account_from_id(self, id: str) -> dict:
        account = await self.account_collection.find_one({"_id": ObjectId(id)})
        if account:
            return self.account_helper(account)
        else:
            return None

    async def update_account(self, id: str, data_update: AccountModel) -> dict:
        account = await self.account_collection.find_one({"_id": ObjectId(id)})

        if account:
            await self.account_collection.update_one(
                {"_id": ObjectId(id)},
                {
                    "$set": {
                        "title": data_update.title,
                        "description": data_update.description,
                        "value": data_update.value,
                        "category": data_update.category,
                        "type_account": data_update.type_account,
                    }
                },
            )

            update_account = await self.account_collection.find_one(
                {"_id": ObjectId(id)}
            )
            return self.account_helper(update_account)

    async def delete_account(self, id: str):
        account = await self.account_collection.find_one({"_id": ObjectId(id)})

        if account:
            return await self.account_collection.delete_one({"_id": ObjectId(id)})
