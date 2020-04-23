import pymongo
import os
from passlib.hash import pbkdf2_sha256
from dotenv import load_dotenv
load_dotenv()

email = input("Email: ")
password = input("Password: ")

encrypted_password = pbkdf2_sha256.hash(password)


client = pymongo.MongoClient(os.environ.get('MONGO_URI'))
client['my_app']['users'].insert_one({
    'email':email,
    'password':encrypted_password
})

print ("User created")