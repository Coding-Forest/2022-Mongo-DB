# 2022-Mongo-DB

Mongo DB learn forest

<br>

### Notes

I learned with the Tutorial by ARC Tutorials. Reference available below. 

<br>

### Content

[[Setup]](#setup)   
[[Basics]](#basics)   

  - Document  
  - Collection  
  - DB 

[[🧭Compass]](#compass)  
[[CMD]](#cmd)  
[[]](#)  
[[]](#)  
[[]](#)  
[[]](#)  
[[References]](#ref)   


<br>

### <span id='setup'>Setup</span>

[[☝️top]](#top)

Option 1. Community Server

1. Download community server from https://www.mongodb.com/try/download/community
2. During install, also install Mongo DB Compass🧭 (the official handy GUI DB admin tool)

<br>

Option 2. Visual Studio Extension

1. Install `Mongo DB for VS Code`
2. Connect to the localhost db `mongodb://127.0.0.1:27017`

<br>

## <span id="basics">Basics</span>

[[☝️top]](#top)

MongoDB is a NoSQL DBMS.

  - No joins
  - No relational structure

<br>

Document 
- Every `document` has a unique value of Key `"_id"`.
  - `"_id": `
- `document`: consists of `key-value` pairs.

Collections
- A group of MongoDB `documents`
- Can have any number of documents.
- `Dynamic schema`: Does not have a schema definition (Collection does not enforce any schema).
- No `join` in `NoSQL`

Database
db
- In MongoDB, `Database` is a physical container of multiple `collections`. 
- Each database has its own file system. 

<br>

Datatypes
- String, Integer ... 
- BSON (Binary-encoded JSON)
  - Date
  - Object id
  - Timestamp
- Code

<br>

## <span id="compass">🧭Compass</span>

[[☝️top]](#top)

- Default credential: `localhost:27017`
- Default DBs: `admin`, `config`, `local`

On VS Code
- `C:\Program Files\MongoDB\Server\5.0\bin\mongo.exe`

<br>

## <span id="cmd">CMD</span>

[[☝️top]](#top)


Database 

- `show databases`: list all db
- `use [database]`
  - select db workspace as current working db
  - create db if it doesn't exist. 
- `db`: show the current working db

  - Drop database
    - `use [database]`: to delete, you have to first select it.
    - `db.dropDatabase()`: delete db

<br>

Collections

- `db.createCollection("collection name")`
- `db.collection.drop()`
- `show collections`

<br>

Documents 

- Insert
  - `db.collection.insert({"key":"value"})`
  - `db.collection.insertMany([{"key":"value"}, {"key":"value"}, ...])`

        db.collection.insertMany([
            {"key":"value"}, 
            {"key":"value"},  
            {"key":"value"}, 
        ])

- Update
  - `db.collection.update({record to update}, {$set: {update content}})
  - Example
        
        > `db.DisneyFriends.update({"name": "MIny"}, {$set: {"name": "Miny"}})`
        WriteResult({ "nMatched" : 0, "nUpserted" : 0, "nModified" : 0 })

- Remove
  - `db.collection.remove(ObjectId("--"))`

- Find
  - `db.collection.find()`

        { "_id" : ObjectId("61e7efa4988099caebcf4e4a"), "name" : "Seoul" }
        { "_id" : ObjectId("61e7efaf988099caebcf4e4b"), "name" : "Bangalore" }
        { "_id" : ObjectId("61e7efe7988099caebcf4e4c"), "name" : "London" }
        { "_id" : ObjectId("61e7f0f8988099caebcf4e4d"), "name" : "Nice" }
        { "_id" : ObjectId("61e7f0f8988099caebcf4e4e"), "name" : "Barcelona" }
        { "_id" : ObjectId("61e7f0f8988099caebcf4e4f"), "name" : "Bangkok" }
        { "_id" : ObjectId("61e7f0f8988099caebcf4e50"), "name" : "Buenos Aires" }
        { "_id" : ObjectId("61e7f0f8988099caebcf4e51"), "name" : "Rio de Janeiro" }

<br>

## <span id=""></span>

[[☝️top]](#top)

<br>

## <span id=""></span>

[[☝️top]](#top)

<br>

## <span id=""></span>

[[☝️top]](#top)

<br>

## <span id=""></span>

[[☝️top]](#top)

<br>

## <span id=""></span>

[[☝️top]](#top)

<br>




### <span id="ref">References</span>

[[☝️top]](#top)

  - ARC Tutorials (2020) MongoDB Tutorial For Beginners https://www.youtube.com/watch?v=SBwNOzuJMyY&list=PLp50dWW_m40UWFSV6PTgYzciZJIxgHy7Q&index=2