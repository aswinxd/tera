from pymongo import MongoClient


client = MongoClient("mongodb+srv://bot:bot@cluster0.8vepzds.mongodb.net/?retryWrites=true&w=majority")  
db = client["terabox_bot"]  
users_collection = db["users"]  

def update_user(user_id, data):
    """Update or create a user document."""
    users_collection.update_one(
        {"user_id": user_id}, 
        {"$set": data}, 
        upsert=True
    )

def get_user(user_id):
    """Fetch a user document by user_id."""
    return users_collection.find_one({"user_id": user_id})
