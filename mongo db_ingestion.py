from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB Atlas
uri = "mongodb+srv://rose:rose123@cluster0.xhflltv.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

print("Connected successfully!")

# Select database
db = client["school"]

# Select collection
collection = db["students"]

# Extract data from MongoDB
data = list(collection.find())

# Convert to pandas DataFrame
df = pd.DataFrame(data)

print(df)