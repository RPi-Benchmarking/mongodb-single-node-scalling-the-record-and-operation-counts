# master_thesis
# Performance Evaluation of MongoDB Database in Edge-Cloud Environment

This repo includes all the works that are related to my master thesis.
in my master thesis, we benchmarked the MongoDB database with the YCSB tool as it suits the cloud environment. The experimental tests include a single node, a docker swarm of two nodes, and a docker swarm of five. Then we integrated FIWARE Orion with mongoDB. 
we used Raspberry Pi, which simulates the edge device while the docker swarm simulates the cloud sittings.
- One of the problems we encountered and solved successfully is that in workload D in the run phase, no insert happens as there are conflicts with the already loaded data in the loading phase. we solved the problem by using this command in the loading phase:

  picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb load mongodb -s -P workloads/workloadd -p recordcount=100000 -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/admin"


  and this command in the transaction phase:

picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb run mongodb -s -P workloads/workloadd -p mongodb.url="mongodb://10.0.13.240:27017/admin" -p insertstart=100001 -p operationcount=100000 -p recordcount=100000 -threads 16 

- or change the configuration of the workloadd file in the ycsb directory to 100000 record counts and operations counts and then execute these commands:

- loading phase:

-  picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb load mongodb -s -P workloads/workloadd -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/admin"

-  transaction phase:

-  picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb run mongodb -s -P workloads/workloadd -p mongodb.url="mongodb://10.0.13.240:27017/admin" -p insertstart=100001  -threads 16

-  and this is the approach we used.
  
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
   
sudo pip3 install docker-compose

sudo docker ps

sudo docker-compose up -d

sudo curl localhost:1026/version

sudo curl 192.168.1.241:1026/version

sudo docker-compose -f docker-compose.yml up -d

sudo docker-compose -f docker-compose2.yml down

sudo docker stack deploy -c docker-compose2.yml your_stack_name
sudo docker node ls

1 sudo apt update

2 sudo apt upgrade

sudo docker stack deploy -c docker-compose6.yml my_stack_name

sudo docker stack ls

sudo docker stack rm my_stack_name

sudo apt-get install python3

python3 –version

sudo apt install default-jdk

sudo apt-get clean

sudo docker stack ps my_stack_name

sudo docker swarm init

sudo docker swarm join-token worker

sudo reboot

sudo systemctl restart docker


   ////////////
   
7. we used Python 2.7.9rc1

   
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

10. Install python

    
sudo wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9rc1.tgz

curl -O https://www.python.org/ftp/python/2.7.9/Python-2.7.9rc1.tgz

sudo tar -xzvf Python-2.7.9rc1.tgz

cd Python-2.7.9rc1

./configure

make

sudo make install

python2 –version

………

uname -m

………
Single Rpi
loading phase

administrator@raspberrypi:~/fe $ sudo ./bin/ycsb load mongodb -s -P workloads/workloada -p recordcount=100000 -threads 16 -p mongodb.url="mongodb://192.168.1.52:27017/admin"

transaction phaseadministrator@raspberrypi:~/fe $ sudo ./bin/ycsb run mongodb -s -P workloads/workloada  -p mongodb.url="mongodb://192.168.1.52:27017/admin" -p operationcount=100000 -threads 16

…..
Built docker swarem of 5 rpi

Sudo docker swarm init

sudo docker swarm leave –force
sudo docker node ls

sudo docker swarm leave

sudo docker swarm join --token SWMTKN-1-1tpj1k1ezfczanr7cv77zbqp4e5wpzuz95sl25ijpw01i4eahc-8l6obx3a3ik5ph3ryd20lzb4f 10.0.13.240:2377

sudo docker stack deploy -c docker-compose.yml mongodb_stack

sudo docker stack rm mongodb_stack

…………..

Clean 

sudo docker system prune -af

https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-darwin-x86_64

sudo apt install gnome-terminal

sudo apt-get update

sudo apt-get install ./docker-desktop-<version>-<arch>.deb

..........

Cassanda
loading to single node
sudo ./bin/ycsb load cassandra-cql -s -P workloads/workloada -p recordcount=50000 -threads 16 -p hosts="10.6.0.11" -p port=9042 -p cassandra.username=cassandra -p cassandra.password=cassandra

transaction to sinlge node 
sudo ./bin/ycsb run cassandra-cql -s -P workloads/workloada -p operationcount=50000 -threads 16 -p hosts="10.6.0.11" -p port=9042 -p cassandra.username=cassandra -p cassandra.password=cassandra

...............

we need to make the database and the corresponding table for each record count load as follows:

cqlsh> create keyspace ycsb

    WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 3 };
    
cqlsh> USE ycsb;

cqlsh> create table usertable (

    y_id varchar primary key,
    
    field0 varchar,
    
    field1 varchar,
    
    field2 varchar,
    
    field3 varchar,
    
    field4 varchar,
    
    field5 varchar,
    
    field6 varchar,
    
    field7 varchar,
    
    field8 varchar,
    
    field9 varchar);
.........................
note: updated
for the workloads that have the insert operation:
There is no need to change the command if you change the specific original workload files of ycsb with there record counts and operations counts
and then use the regular command without the insert  at modifications to the command.
for example change the record count to 100000 and the operation count to 100000 in the original workload file and then use this for the loading phase

- picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb load mongodb -s -P workloads/workloadd -p recordcount=100000 -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/admin"

and this command for the transaction phase

- picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb run mongodb -s -P workloads/workloadd  -p mongodb.url="mongodb://10.0.13.240:27017/admin" -p operationcount=100000 -threads 16

- .................

- ssh picocluster@proxy50.rt3.io -p 38958


Links:
1. Cassandra docker-compose:
https://hub.docker.com/r/markusgulden/cassandra-web

2. https://github.com/brianfrankcooper/YCSB/releases


