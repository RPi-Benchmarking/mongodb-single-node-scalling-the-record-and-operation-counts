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
    { _id: 2, host: "mongo_db2:27018" },
    { _id: 3, host: "mongo_db3:27019" },
    { _id: 4, host: "mongo_db4:27020" },
    { _id: 5, host: "mongo_db5:27021" },
    { _id: 6, host: "mongo_db6:27022" },
    { _id: 7, host: "mongo_db7:27023" },
    { _id: 8, host: "mongo_db8:27024" },
    { _id: 9, host: "mongo_db9:27025" },
    { _id: 10, host: "mongo_db10:27026" }
  ]
})



  
