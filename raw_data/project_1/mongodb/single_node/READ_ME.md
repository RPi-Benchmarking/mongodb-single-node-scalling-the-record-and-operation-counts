this directory includes all the raw data to benchmark mongoDB with 60000,70000,80000,90000, and 100000 record counts and operation counts for five trials.
commands:
loading phase: 
sudo ./bin/ycsb load mongodb -s -P workloads/workloada -p recordcount=60000 -threads 16 -p mongodb.url="mongodb://Your_IP:27017/admin"
transaction phase:
sudo ./bin/ycsb run  mongodb -s -P workloads/workloada -p mongodb.url="mongodb://Your_IP:27017/admin" -p operationcount=60000 -threads 16

...........

for workload d we used this command for the loading phase after modifying
the workload D file for the required record count and the operation count
 in our case, we used 60000, 70000, 80000, 90000, and 100000.
for the loading phase we used this command

- picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0/workloads $ sudo ./bin/ycsb load mongodb -s -P workloads/workloadd -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/admin"

for the transaction phase we used this command:

- picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0/workloads $ sudo ./bin/ycsb run mongodb -s -P workloads/workloadd -p mongodb.url="mongodb://10.0.13.240:27017/admin" -p insertstart=100001  -threads 16

..................

loading phase: picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb load mongodb -s -P workloads/workloadc -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/admin"

transaction phase: picocluster64@pc0:~/fe/ycsb-mongodb-binding-0.17.0 $ sudo ./bin/ycsb run mongodb -s -P workloads/workloadd -threads 16 -p mongodb.url="mongodb://10.0.13.240:27017/admin"
