the deployment done following this link: https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/docker/

the command to load the data:

./bin/ycsb load redis -s -P workloads/workloada -p "redis.host=localhost" -p "redis.port=6379"

transaction phase:
./bin/ycsb run redis -s -P workloads/workloada -p "redis.host=localhost" -p "redis.port=6379"
 REDIS web interface:
 
 ![image](https://github.com/user-attachments/assets/d35ef5b3-fe8f-4b5f-81c1-e27bdf3678b0)

after loading 60000 record counts:

![image](https://github.com/user-attachments/assets/8038b159-2dd9-4762-83b9-ccdc2e19c940)

for deploying redis on one node use this command:

sudo docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest


