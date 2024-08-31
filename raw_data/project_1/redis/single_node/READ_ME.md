the deployment done following this link: https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/docker/

the command to load the data:

./bin/ycsb load redis -s -P workloads/workloada -p "redis.host=localhost" -p "redis.port=6379"

transaction phase:
./bin/ycsb run redis -s -P workloads/workloada -p "redis.host=localhost" -p "redis.port=6379"
