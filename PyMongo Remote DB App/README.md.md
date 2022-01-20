# Remote MongoDB setup and integration

<br>

Notes: Access configuration problem. Project on hold.
To resume project, start here at: https://youtu.be/bASNF0uqivM?t=1335

<br>

### Content

[[Setup]](#setup)   
[[AWS EC2: Install MongoDB on virtual instance]](#aws)   
[[AWS EC2: Set up MongoDB server (tutorial)]](#aws2)  
[[PuTTy: MongoDB Setup]](#putty)
[[Python: work with DB]](#python)  
[[]](#)  
[[]](#)  
[[]](#)  
[[References]](#ref)   

<br>

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


## <span id="aws2">AWS EC2: Set up MongoDB server (tutorial)</span>

[[☝️top]](#top)

1. Start an EC2 instance on default settings. 
2. Now on Linux (Ubuntu in this case) terminal: 

    chmod 0400 your_key.pem
    ssh -i your_key.pem ec2-user@public_IP_address

3. Update packages

    sudo yum update -y


4. Install Mongo DB. 

  - Trouble shoot

        $ sudo yum install mongodb-org

        Loaded plugins: priorities, update-motd, upgrade-helper
        No package mongodb-org available.
        Error: Nothing to do

  - Solution: Create a `/etc/yum.repos.d/mongodb-org-5.0.repo` file so that you can install MongoDB directly using yum:
  
        sudo vi /etc/yum.repos.d/mongodb-org-5.0.repo

        [mongodb-org-5.0]
        name=MongoDB Repository
        baseurl=https://repo.mongodb.org/yum/amazon/2/mongodb-org/5.0/x86_64/
        gpgcheck=1
        enabled=1
        gpgkey=https://www.mongodb.org/static/pgp/server-5.0.asc
  
  - Delete file

        sdo rm -r /file_path/

<br>

5. Now install for real.

        sudo yum install -y mongodb-org

        Installed:
          mongodb-org.x86_64 0:5.0.5-1.amzn2                                                               

        Dependency Installed:
          cyrus-sasl.x86_64 0:2.1.26-23.amzn2                                                              
          cyrus-sasl-gssapi.x86_64 0:2.1.26-23.amzn2                                                       
          mongodb-database-tools.x86_64 0:100.5.1-1                                                        
          mongodb-mongosh.x86_64 0:1.1.9-1.el7                                                             
          mongodb-org-database.x86_64 0:5.0.5-1.amzn2                                                      
          mongodb-org-database-tools-extra.x86_64 0:5.0.5-1.amzn2                                          
          mongodb-org-mongos.x86_64 0:5.0.5-1.amzn2                                                        
          mongodb-org-server.x86_64 0:5.0.5-1.amzn2                                                        
          mongodb-org-shell.x86_64 0:5.0.5-1.amzn2                                                         
          mongodb-org-tools.x86_64 0:5.0.5-1.amzn2                                                         

        Complete!

6. Configure to auto-start on reboot.

        sudo chkconfig mongod on

7. Start MongoDB!

        mongo

<br>

8. Configure access (config file fiddle)


        sudo vi /etc/mongod.conf

        # network interfaces
        net:
          port: 27017
          bindIp: 127.0.0.1  >> 0.0.0.0
        # Enter 0.0.0.0,:: to bind to all IPv4 and IPv6 addresses or, alternatively, use the net.bindIpAll setting.

9. [AWS] Change security group inbound rules

- Add the following: 

        Type: Custom TCP
        Port range: 27017 (this is MongoDB default port)
        Source: 0.0.0.0/0 (Anywhere)
        Description - optional: mongodb


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