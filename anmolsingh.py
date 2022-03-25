# Install Pymongo[srv] : pip install pymongo[srv]
import pymongo

# Connect to the Database on cloud
myclient = pymongo.MongoClient("mongodb+srv://anmolsingh:anmol.1811@cluster0.02c5e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create Database
test_db = myclient["testDatabase"]

test_collection = test_db["Movies"]

movies_list = [
    { "name" : "Puaada", "actor": "Ammy Virk", "actress": "Sargun Mehta", "director": "Rupinder Chahal", "year": 2021},
    { "name" : "Qismat 2", "actor": "Ammy Virk", "actress": "Sonam Bajwa", "director" : "Jagdeep Sidhu", "year": 2021},
    { "name" : "Yaar Anmulle Returns", "actor": "Prabh Gill", "actress": "Jasleen Slaich", "director" : "Harry Bhatti", "year": 2021},
    { "name" : "Posti", "actor": "Babbal Rai", "actress": "Surilie Gautam", "director" : "Rana Ranbir", "year": 2022},    
    { "name" : "Jinde Meriye", "actor": "Parmish Verma", "actress": "Sonam Bajwa", "director" : "Pankaj Batra", "year": 2020},
]

data = test_collection.insert_many(movies_list)

retrieve_data = test_collection.find () # equivalent to SELECT * FROM table_name

for item in retrieve_data:
    print(item)