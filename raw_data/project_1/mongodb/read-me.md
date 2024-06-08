# Container Virtualization on the Edge Node with NoSQL databases: A performance evaluation
docker service ps <service-name>
docker service logs <service-name>
docker service scale <service-name>=<desired-number-of-replicas>
docker service scale my_stack_name_mongo_db=3
docker service scale my_stack_name_mongo_db=5
docker service ls
docker service ps my_stack_name_mongo_db
version: '3.7'

services:
  mongo_db:
    image: mongo:4.2.12
    ports:
      - "27017:27017"
    deploy:
      replicas: 5

  mongo_express:
    image: mongo-express:0.54.0
    ports:
      - "8081:8081"
    deploy:
      replicas: 1

volumes:
  mongo-data:

  ............

sudo docker network create --driver overlay proxy
sudo docker network ls

............

for the bash 

rs.initiate({
  _id: "test-rs",
  members: [
    { _id: 1, host: "mongo_db1:27017" },
    { _id: 2, host: "mongo_db2:27017" },
    { _id: 3, host: "mongo_db3:27017" },
    { _id: 4, host: "mongo_db4:27017" },
    { _id: 5, host: "mongo_db5:27017" },
    { _id: 6, host: "mongo_db6:27017" },
    { _id: 7, host: "mongo_db7:27017" },
    { _id: 8, host: "mongo_db8:27017" },
    { _id: 9, host: "mongo_db9:27017" },
    { _id: 10, host: "mongo_db10:27017" }
  ]
})

..................

var config = rs.conf();

// Modify the configuration as needed
config.members = [
  { _id: 1, host: "mongo_db1:27017" },
  { _id: 2, host: "mongo_db2:27017" },
  { _id: 3, host: "mongo_db3:27017" },
  { _id: 4, host: "mongo_db4:27017" },
  { _id: 5, host: "mongo_db5:27017" },
  { _id: 6, host: "mongo_db6:27017" },
  { _id: 7, host: "mongo_db7:27017" },
  { _id: 8, host: "mongo_db8:27017", votes: 0, priority: 0 },
  { _id: 9, host: "mongo_db9:27017", votes: 0, priority: 0 },
  { _id: 10, host: "mongo_db10:27017", votes: 0, priority: 0 }
];

// Reconfigure the replica set
rs.reconfig(config)

..............


var config = rs.conf();


// Modify the configuration as needed

config.members = [
  { _id: 1, host: "mongo_db1:27017" },
  { _id: 2, host: "mongo_db2:27017" },
  { _id: 3, host: "mongo_db3:27017" },
  { _id: 4, host: "mongo_db4:27017" },
  { _id: 5, host: "mongo_db5:27017" },
  { _id: 6, host: "mongo_db6:27017" },
  { _id: 7, host: "mongo_db7:27017" },
  { _id: 8, host: "mongo_db8:27017"},
  { _id: 9, host: "mongo_db9:27017"},
  { _id: 10, host: "mongo_db10:27017"}
];

// Reconfigure the replica set

rs.reconfig(config)


.........................


test-rs:PRIMARY> // Reconfigure the replica set
test-rs:PRIMARY> var config = rs.conf();
test-rs:PRIMARY>
test-rs:PRIMARY> // Modify the configuration as needed
test-rs:PRIMARY>
test-rs:PRIMARY> config.members = [ { _id: 1, host: "mongo_db1:27017" }, { _id: 2, host: "mongo_db2:27017" }, { _id: 3, host: "mongo_db3:27017" }, { _id: 4, host: "mongo_db4:27017" }, { _id: 5, host: "mongo_db5:27017" }, { _id: 6, host: "mongo_db6:27017" }, { _id: 7, host: "mongo_db7:27017" }, { _id: 8, host: "mongo_db8:27017"}, { _id: 9, host: "mongo_db9:27017"}, { _id: 10, host: "mongo_db10:27017"} ];
[
        {
                "_id" : 1,
                "host" : "mongo_db1:27017"
        },
        {
                "_id" : 2,
                "host" : "mongo_db2:27017"
        },
        {
                "_id" : 3,
                "host" : "mongo_db3:27017"
        },
        {
                "_id" : 4,
                "host" : "mongo_db4:27017"
        },
        {
                "_id" : 5,
                "host" : "mongo_db5:27017"
        },
        {
                "_id" : 6,
                "host" : "mongo_db6:27017"
        },
        {
                "_id" : 7,
                "host" : "mongo_db7:27017"
        },
        {
                "_id" : 8,
                "host" : "mongo_db8:27017"
        },
        {
                "_id" : 9,
                "host" : "mongo_db9:27017"
        },
        {
                "_id" : 10,
                "host" : "mongo_db10:27017"
        }
]
test-rs:PRIMARY>
test-rs:PRIMARY> // Reconfigure the replica set
test-rs:PRIMARY>
test-rs:PRIMARY> rs.reconfig(config)
{
        "operationTime" : Timestamp(1717621035, 1),
        "ok" : 0,
        "errmsg" : "Replica set configuration contains 10 voting members, but must be at least 1 and no more than 7",
        "code" : 103,
        "codeName" : "NewReplicaSetConfigurationIncompatible",
        "$clusterTime" : {
                "clusterTime" : Timestamp(1717621035, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        }
}
test-rs:PRIMARY>

...............

rs.initiate({
  _id: "test-rs",
  members: [
    { _id: 1, host: "mongo_db1:27017" },
    { _id: 2, host: "mongo_db2:27018" },
    { _id: 3, host: "mongo_db3:27019" },
    { _id: 4, host: "mongo_db4:27020" },
    { _id: 5, host: "mongo_db5:27021" },
    { _id: 6, host: "mongo_db6:27022" },
    { _id: 7, host: "mongo_db7:27023" },
    { _id: 8, host: "mongo_db8:27024", votes: 0, priority: 0 },
    { _id: 9, host: "mongo_db9:27025", votes: 0, priority: 0 },
    { _id: 10, host: "mongo_db10:27026", votes: 0, priority: 0 }
  ]
})

...............

var config = rs.conf();

// Modify the configuration as needed

config.members = [ { _id: 1, host: "mongo_db1:27017" }, { _id: 2, host: "mongo_db2:27017" }, { _id: 3, host: "mongo_db3:27017" }, { _id: 4, host: "mongo_db4:27017" }, { _id: 5, host: "mongo_db5:27017" }, { _id: 6, host: "mongo_db6:27017" }, { _id: 7, host: "mongo_db7:27017" }, { _id: 8, host: "mongo_db8:27017", votes: 0, priority: 0}, { _id: 9, host: "mongo_db9:27017", votes: 0, priority: 0}, { _id: 10, host: "mongo_db10:27017", votes: 0, priority: 0} ];

// Reconfigure the replica set

rs.reconfig(config)

...........

rs.status();

...................



![image](https://github.com/SaraDanaKablTalabani/master_thesis/assets/101463904/3cc0420b-a0a5-4ac7-ac96-0c7bd93ca242)



......

![image](https://github.com/SaraDanaKablTalabani/master_thesis/assets/101463904/1bae7ac2-dc38-453b-8361-0b6ddc2cee47)

...........

rs.initiate({
  _id: "test-rs",
  members: [
    { _id: 1, host: "mongo_db1:27017" },
    { _id: 2, host: "mongo_db2:27017" },
    { _id: 3, host: "mongo_db3:27017" },
    { _id: 4, host: "mongo_db4:27017" },
    { _id: 5, host: "mongo_db5:27017" },
    { _id: 6, host: "mongo_db6:27017" },
    { _id: 7, host: "mongo_db7:27017" },
    { _id: 8, host: "mongo_db8:27017", votes: 0, priority: 0 },
    { _id: 9, host: "mongo_db9:27017", votes: 0, priority: 0 },
    { _id: 10, host: "mongo_db10:27017", votes: 0, priority: 0 }
  ]
})

.........................

rs.reconfig(config, { force: true })

links
1.https://www.mongodb.com/docs/manual/sharding/#:~:text=Sharding%20is%20a%20method%20for,capacity%20of%20a%20single%20server.

2. https://github.com/yasasdy/mongodb-sharding 










  
