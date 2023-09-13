import os

from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() # take .env variables

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')

uri = f"mongodb://{user}:{password}@ac-3urhvqt-shard-00-00.lmqzxid.mongodb.net:27017,ac-3urhvqt-shard-00-01.lmqzxid.mongodb.net:27017,ac-3urhvqt-shard-00-02.lmqzxid.mongodb.net:27017/?ssl=true&replicaSet=atlas-lt75me-shard-0&authSource=admin&retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client.get_database('prueba').get_collection('david').insert_one(document={"marca": "opel", "modelo": "omega"})
