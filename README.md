# master_thesis
this repo includes all the works which are related to my master thesis.
we used Raspberry Pi
1. to load a record count of 5000 to the manager node, we used this command: sudo ./bin/ycsb load mongodb -s -P workloads/workloadd -p recordcount=5000 -threads 16 -p mongodb.url="mongodb://10.0.13.230:27017/ycsb_data_manager"

2. to load a record count tho the single pi setup, we used this command: sudo ./bin/ycsb load mongodb -s -P workloads/workloada -p recordcount=100000 -threads 16 -p mongodb.url="mongodb://192.168.1.52:27017/admin"

3. The orion version which we used is 3.12.0-next, rasbpery pi 4 Model B 8GB LPDDR RAM, 64-bit quad-core Cortex-A72 processor, 
