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
