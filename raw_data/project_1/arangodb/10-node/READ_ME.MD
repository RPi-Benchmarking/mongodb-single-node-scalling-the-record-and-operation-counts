sudo docker service scale sara2_arangodb_db_container=3

sudo docker run -d arangodb/arangodb-starter     --starter.address=10.0.13.242     --starter.join 10.0.13.241:8529,10.0.13.240:8529

arangosh --server.endpoint tcp://10.0.13.240:8529 --server.username root --server.password rootpassword

links:
https://github.com/Dumstruck/arango-swarm
https://github.com/arangodb/arangodb/issues/4602


