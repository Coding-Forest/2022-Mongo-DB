import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://atlasuser:atlas1234@cluster0.t2e26.mongodb.net/test?retryWrites=true&w=majority")

# cluster (database) > collection > document (post)

# Set up DB
db = cluster["test_db"]
collection = db["test_collection"]


# insert one post
post1 = {"name": "MongoDB", "project": "MongoDB using pymongo", "hours": 0.5}
post2 = {"tech": "Docker", "project": "Docker for beginers", "hours": 3}
post3 = {"tech": "Docker", "project": "Docker with kodekloud", "hours": 2}

posts = [post1, post2, post3]

for post in posts:
    collection.insert_one(post)


# insert many posts
post1 = {"name": "Kubernetes", "project": "Kubernetes for beginners", "hours": 1}
post2 = {"tech": "AWS", "project": "Cloud Practitioner", "hours": 50}
post3 = {"tech": "tkinter", "project": "tkinter for beginners", "hours": 5}

collection.insert_many([post1, post2, post3]) 


## Furnish db with some more data
post1 = {"tech": "Data structure", "project": "major course", "weeks": 9}
post2 = {"name": "MongoDB", "project": "MongoDB using pymongo", "hours": 0.5}
post3 = {"name": "Kubernetes", "project": "Kubernetes for beginners", "hours": 1}

results = collection.insert_many([post1, post2, post3])


# QUERY
# find
results = collection.find({'tech': "Docker"})

for result in results:
    print(result)

# find_one
result = collection.find_one({"_id": 1})

print(result)


# find all records
results = collection.find()
for r in results:
    print(r)


# DELETE
# delete_one
results = collection.delete_one({"_id": 0})

# delete_many
post1 = {"name": "Kubernetes"}
post2 = {"name": "Data structure"}
post3 = {"name": "MongoDB"}

query = {"name": {"$regex": "Kubernetes|Data structure|MongoDB"}}

collection.delete_many(query)


# UPDATE
# update_one
results = collection.update_one({"_id":2}, {"$set": {"project": "Docker for beginners"}})


# update_many
collection.update_many({"project": "major course"}, {"$inc":{"weeks": -4}})


post_count = collection.count_documents({})

print(post_count)