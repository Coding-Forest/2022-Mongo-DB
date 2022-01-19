# Python MongoDB using PyMongo

Learn MongoDB + pymongo

<br>

### Notes

I learned with the Tutorial by ARC Tutorials. Reference available below. 

<br>

### Content

[[Setup]](#setup)   
[[Basics]](#basics)   
[[pymongo]](#pymongo)  
[[References]](#ref)   


<br>

### <span id='setup'>Setup</span>

[[☝️top]](#top)

1. Create an account at cloud.mongodb.com
2. Sign in and create a `cluster` (database). 
3. Create a `collection`.
  - Configure security. 
    - Grant access to User and IP

<br>

## <span id="basics">Basics</span>

[[☝️top]](#top)

4. Connect to your database. 
  - Add a connection IP address (`whitelist IPs`).
  - Create a `Database User`.
5. On `connect your application` tab, 
  - change `driver` to `Python`
  - copy `mongodb+srv://username:<password>@cluster_name.t2e26.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`

<br>

    pymongo.errors.ConfigurationError: The "dnspython" module must be installed to use mongodb+srv:// URIs. To fix this error install pymongo with the srv extra:
    C:\Users\0woo0\PycharmProjects\crawler\venv\Scripts\python.exe -m pip install "pymongo[srv]"

6. `pip install pymongo[srv]`



<br>

## <span id="pymongo">`pymongo`</span>

[[☝️top]](#top)

`INSERT`

- `collection.insert_one(post)`
- `collection.insert_many(post)`

<br>

`QUERY`

- `collection.find_one({key:value})`
- `collection.find({key:value})`
- `collection.find()`: find all records.

Example

- `collection.find({'_id': 1})`

      {'_id': 1, 'name': 'MongoDB', 'project': 'MongoDB using pymongo', 'hours': 0.5}

- `collection.find({'tech': "Docker"})`

      {'_id': 2, 'tech': 'Docker', 'project': 'Docker for beginers', 'hours': 3}
      {'_id': 3, 'tech': 'Docker', 'project': 'Docker with kodekloud', 'hours': 2}

<br>

`DELETE`

- `collection.delete_one({key: value})`
- `collection.delete_many({key: {"$regex": "regular_expression for your query"}})`

Example

- `query = {"name": {"$regex": "Kubernetes|Data structure|MongoDB"}}`

<br>

`UPDATE`

- `collection.update_one({"key":value}, {"$set": {"key": "value"}})`
- `collection.update_many({"key":value}, {"$set": {"key": "value"}})`

Example

- `collection.update_one({"_id":2}, {"$set": {"project": "Docker for beginners"}})`

<br>

Count documents

- `collection.count_documents({})`: count all documents

<br>

### <span id="ref">References</span>

[[☝️top]](#top)

  - Tech With Tim (2019) Python MongoDB Tutorial using PyMongo https://www.youtube.com/watch?v=rE_bJl2GAY8
