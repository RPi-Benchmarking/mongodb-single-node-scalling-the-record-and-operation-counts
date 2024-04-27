# master_thesis
this repo includes all the works which are related to my master thesis.
we used Raspberry Pi
1. to load a record count of 5000 to the manager node, we used this command: sudo ./bin/ycsb load mongodb -s -P workloads/workloadd -p recordcount=5000 -threads 16 -p mongodb.url="mongodb://10.0.13.230:27017/ycsb_data_manager"

2. to load a record count tho the single pi setup, we used this command: sudo ./bin/ycsb load mongodb -s -P workloads/workloada -p recordcount=100000 -threads 16 -p mongodb.url="mongodb://192.168.1.52:27017/admin"

3. The orion version which we used is 3.12.0-next, rasbpery pi 4 Model B 8GB LPDDR RAM, 64-bit quad-core Cortex-A72 processor, 
4. we used Yahoo! Cloud System Benchmark.
   /////////////////////////////////////////////////////////////////////////
5. Commands:
Cluster:
   load:
maanger
   administrator@raspberrypi:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb load mongodb -s -P workloads/workloadc -p recordcount=30000 -threads 16 -p mongodb.url="mongodb://192.168.1.182:27017/ycsb_data_manager"
...................
   worker
   sudo ./bin/ycsb load mongodb -s -P workloads/workloadc -p recordcount=50000 -threads 16 -p mongodb.url="mongodb://192.168.1.196:27017/ycsb_data_worker"
   ..............................
   transaction:
   manager:
   sudo ./bin/ycsb run  mongodb -s -P workloads/workloadc -p mongodb.url="mongodb://192.168.1.182:27017/ycsb_data_manager" -p operationcount=20000 -threads 16
   ..............
   worker:
   sudo ./bin/ycsb run  mongodb -s -P workloads/workloadc -p mongodb.url="mongodb://192.168.1.196:27017/ycsb_data_worker" -p operationcount=40000 -threads 16
   /////////////////////////////
6. we used Python 2.7.9rc1

   
////////////////////

MongoDB

Commands:

sudo systemctl restart docker

sudo wget https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-mongodb-binding-0.17.0.tar.gz

sudo tar xvf ycsb-mongodb-binding-0.17.0.tar.gz

cd ycsb-mongodb-binding-0.17.0


////////
Cassandra

1. [04/27/24]seed@VM:~/fe$ sudo wget --no-check-certificate https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-cassandra-binding-0.17.0.tar.gz

install cassandra binding:  https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-cassandra-binding-0.17.0.tar.gz

2. sudo tar xvf ycsb-cassandra-binding-0.17.0.tar.gz

3. cd ycsb-cassandra-binding-0.17.0

4. to know the ip for the raspberry pi: hostname -I

5. sudo apt update

6. sudo apt upgrade

7. sudo pip3 install docker-compose
docker-compose –version

8. sudo apt-get purge openjdk-11-jre-headless
sudo apt-get install openjdk-11-jre-headless
sudo apt-get install openjdk-11-jre

9. ssh-keygen -R 192.168.1.241




version: '3.7'

services:
  cassandra_db:
    image: cassandra:latest
    ports:
      - 9042:9042
    volumes:
      - /C/Mine/cassandraData:/var/lib/cassandra

  cassandra_web:
    image: katanas/cassandra-web:latest
    environment:
      - DATABASE_HOST=cassandra_db
      - DATABASE_PORT=9042
    ports:
      - "3000:3000"
    restart: on-failure
    depends_on:
      - cassandra_db




