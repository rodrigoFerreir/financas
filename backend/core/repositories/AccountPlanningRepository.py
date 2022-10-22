from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

from decouple import config
from models import AccountPlanningModel


MONGO_DB_URL = config("MONGO_DB_URL")


client_db = AsyncIOMotorClient(MONGO_DB_URL)


class AccountRepository:
    database = client_db.financas

    account_planning_collection = database.get_collection("account")

    def account_planning_helper(self, account) -> dict:
        return {
            "_id": str(account["_id"]),
            "name": str(account["name"]),
            "descript": str(account["descript"]),
            "type_account_planning": str(account["type_account_planning"]),
        }

    async def save_account(self, account: AccountPlanningModel) -> dict:
        new_account = await self.account_planning_collection.insert_one(
            account.__dict__
        )

        get_new_account = await self.account_planning_collection.find_one(
            {"_id": new_account.inserted_id}
        )

        return self.account_planning_helper(get_new_account)

    async def list_all_accounts(self):
        accounts = self.account_planning_collection.aggregate(
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
            all_accounts.append(self.account_planning_helper(account))

        return all_accounts

    async def list_account_from_id(self, id: str) -> dict:
        account = await self.account_planning_collection.find_one({"_id": ObjectId(id)})
        if account:
            return self.account_planning_helper(account)
        else:
            return None

    async def update_account(self, id: str, data_update: AccountPlanningModel) -> dict:
        account = await self.account_planning_collection.find_one({"_id": ObjectId(id)})

        if account:
            await self.account_planning_collection.update_one(
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

            update_account = await self.account_planning_collection.find_one(
                {"_id": ObjectId(id)}
            )
            return self.account_planning_helper(update_account)

    async def delete_account(self, id: str):
        account = await self.account_planning_collection.find_one({"_id": ObjectId(id)})

        if account:
            return await self.account_planning_collection.delete_one(
                {"_id": ObjectId(id)}
            )
