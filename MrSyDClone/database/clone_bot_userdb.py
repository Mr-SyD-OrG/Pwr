import motor.motor_asyncio
from info import CLONE_DATABASE_URI, DATABASE_NAME
from info import AUTH_CHANNEL, DATABASE_URI
import logging


logger = logging.getLogger(__name__)

class JoinReqs:
    def __init__(self, bot_id, auth_channel):
        self.bot_id = bot_id
        self.auth_channel = auth_channel

        if DATABASE_URI:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI)
            self.db = self.client["JoinReqs"]
            self.col = self.db[str(self.auth_channel)]
        else:
            self.client = None
            self.db = None
            self.col = None

    def isActive(self):
        return self.client is not None

    async def add_user(self, user_id, first_name, username, date):
        try:
            result = await self.col.insert_one({
                "_id": f"{self.bot_id}_{user_id}",  # Unique ID with bot_id
                "bot_id": self.bot_id,
                "user_id": int(user_id),
                "first_name": first_name,
                "username": username,
                "date": date
            })
            logger.info("User added with ID %s", result.inserted_id)
        except Exception as e:
            logger.error("Failed to add user %s: %s", user_id, e)

    async def get_user(self, user_id):
        try:
            user = await self.col.find_one({"user_id": int(user_id), "bot_id": self.bot_id})
            if user:
                logger.info("User found: %s", user)
            else:
                logger.warning("User %s not found", user_id)
            return user
        except Exception as e:
            logger.error("Error fetching user %s: %s", user_id, e)
            return None
            
    async def get_all_users(self):
        # Include bot_id in the filter
        return await self.col.find({"bot_id": self.bot_id}).to_list(None)

    async def delete_user(self, user_id):
        # Include bot_id in the filter
        await self.col.delete_one({"user_id": int(user_id), "bot_id": self.bot_id})

    async def delete_all_users(self):
        # Include bot_id in the filter
        await self.col.delete_many({"bot_id": self.bot_id})

    async def get_all_users_count(self): 
        # Include bot_id in the filter
        return await self.col.count_documents({"bot_id": self.bot_id})


class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.req = self.db.requests

    async def find_join_req(self, id):
        return bool(await self.req.find_one({'id': id}))
        
    async def add_join_req(self, id):
        await self.req.insert_one({'id': id})
    async def del_join_req(self):
        await self.req.drop()
        
    async def add_user(self, bot_id, user_id):
        user = {'user_id': int(user_id)}
        await self.db[str(bot_id)].insert_one(user)
    
    async def is_user_exist(self, bot_id, id):
        user = await self.db[str(bot_id)].find_one({'user_id': int(id)})
        return bool(user)
    
    async def total_users_count(self, bot_id):
        count = await self.db[str(bot_id)].count_documents({})
        return count

    async def get_all_users(self, bot_id):
        return self.db[str(bot_id)].find({})

    async def delete_user(self, bot_id, user_id):
        await self.db[str(bot_id)].delete_many({'user_id': int(user_id)})


clonedb = Database(CLONE_DATABASE_URI, DATABASE_NAME)
