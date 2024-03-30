# master_thesis
this repo includes all the works which are related to the master thesis.
we used Raspberry Pi
1. to load a record count of 5000 to the manager node, we used this command:  sudo ./bin/ycsb load mongodb -s -P workloads/workloadd -p recordcount=5000 -threads 16 -p mongodb.url="mongodb://10.0.13.230:27017/ycsb_data_manager"

2. 
