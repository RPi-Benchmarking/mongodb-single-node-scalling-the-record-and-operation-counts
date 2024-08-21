the commmand to load: picocluster64@pc24:~/fe5/ycsb-cassandra-binding-0.17.0 $ sudo ./bin/ycsb load cassandra-cql -s -P workloads/workloada -threads 16 -p hosts="10.0.13.234" -p port=9042 -p cassandra.username=admin -p cassandra.password=admin

transaction: picocluster64@pc24:~/fe5/ycsb-cassandra-binding-0.17.0 $ sudo ./bin/ycsb run cassandra-cql -s -P workloads/workloada -threads 16 -p hosts="10.0.13.234" -p port=9042 -p cassandra.username=admin -p cassandra.password=admin

USE ycsb;

TRUNCATE usertable;

verify

SELECT * FROM usertable;

.........

cqlsh> create keyspace ycsb  WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1 };

cqlsh> USE ycsb;
cqlsh:ycsb> create table usertable (
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

.............
