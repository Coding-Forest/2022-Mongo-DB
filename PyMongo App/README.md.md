# Remote MongoDB setup and integration

<br>


### Content

[[Setup]](#setup)   
[[AWS EC2: Install MongoDB on virtual instance]](#aws)   
[[PuTTy: MongoDB Setup]](#putty)
[[Python: work with DB]](#python)  
[[]](#)  
[[]](#)  
[[]](#)  
[[]](#)  
[[References]](#ref)   


<br>

### <span id='setup'>Setup</span>

[[☝️top]](#top)

1. AWS
2. MongoDB
3. PuTTy

<br>

1-1. Run a `ubuntu` instance (FreeTier).
3-1. Copy the Public IP, login using PuTTY. 
  - `public IP`
  - `login as: admin`

<br>
<br>

## <span id="aws">AWS EC2: Install MongoDB on virtual instance (`Ubuntu`)</span>

[[☝️top]](#top)

Log in to the `ubuntu` instance.

    login as: ubuntu

Install dependencies required to add a new repository over HTTPS.

    sudo apt update
    sudo apt install dirmngr gnupg apt-transport-https ca-certificates software-properties-common

Import the repository’s GPG key and add the MongoDB repository with:

    wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
    sudo add-apt-repository 'deb [arch=amd64] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse'

<br>

Once the repository is enabled, install the mongodb-org meta-package.

    sudo apt install mongodb-org

Installed packages:
  - `mongodb-org-server`: daemon, `init scripts` and configurations
  - `mongodb-org-mongos`: daemon
  - `mongodb-org-shell`: mongo shell
  - `mongodb-org-tools`: MongoDB tool set used to import and export data, statistics and some other utilities

<br>

Start `MongoDB` daemon

    sudo systemctl enable --now mongod

(Optional) installation result verification command

    mongo --eval 'db.runCommand({ connectionStatus: 1 })'

<br>

**Configuration**

    sudo nano /etc/mongod.conf

    /etc/mongod.conf
    security:
      authorization: enabled

    sudo systemctl restart mongod


https://linuxize.com/post/how-to-install-mongodb-on-ubuntu-20-04/

<br>
<br>

## <span id="putty">PuTTy: MongoDB Setup</span>

[[☝️top]](#top)

Create user

    db.createUser({user: "ubuntu", pw": "ubuntu", roles: [{role: "readWrite", db:"dealership"}]})

    Successfully added user: {
            "user" : "ubuntu",
            "roles" : [
                    {
                            "role" : "readWrite",
                            "db" : "dealership"
                    }
            ]
    }

<br>

Configure access (IP address)

    mongo nano /etc/mongod.conf

    /etc/mongod.conf
    ...
    net:
      port: 27017
      bindIp: 0.0.0.0
    ...
    security:
      authorization: 'enabled'
    

Restart MongoDB

    sudo service mongod restart

<br>
<br>

## <span id="python">Python: work with DB</span>

[[☝️top]](#top)

Connect to MongoDB database running on Ubuntu EC2 instance.
The below client can only read and write to database 'dealership' as per mongod.conf.


    client = pymongo.MongoClient('mongodb://username:password@IP_address/')

    db = client["dealership"]

    Process finished with exit code 0

<br>

Database structure

    Database
      Collection
        Document



<br>

## <span id=""></span>

[[☝️top]](#top)

<br>

## <span id=""></span>

[[☝️top]](#top)

<br>



### <span id="ref">References</span>

[[☝️top]](#top)

  - Tech With Tim (2020) Python Database Project #1 - Remote MongoDB Setup & Integration https://www.youtube.com/watch?v=bASNF0uqivM&t=59s