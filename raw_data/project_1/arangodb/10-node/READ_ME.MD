sudo docker service scale sara2_arangodb_db_container=3

sudo docker run -d arangodb/arangodb-starter     --starter.address=10.0.13.242     --starter.join 10.0.13.241:8529,10.0.13.240:8529
