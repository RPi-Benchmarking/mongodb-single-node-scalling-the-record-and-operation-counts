commands:

sudo systemctl restart docker
sudo docker swarm leave --force
Sudo docker swarm init
sudo docker node ls
sudo docker-compose -f docker-compose.yml up -d
sudo docker-compose -f docker-compose2.yml down
sudo docker stack deploy -c docker-compose2.yml my_stack_name
sudo reboot

after executing these commands  with the given .yml file, the cluster of nodes should all be up and working. 

.............
labeling placement constraints

docker node update --label-add mongo=replica <worker-node-id>

docker node update --label-add mongo=manager <manager-node-id>

 sudo docker node update --label-add mongo=manager pc0

sudo docker node update --label-add mongo=replica pc0

sudo docker node update --label-add mongo=replica pc1

sudo docker node update --label-add mongo=replica pc2

sudo docker node update --label-add mongo=replica pc3

sudo docker node update --label-add mongo=replica pc4


.................

labeling placement preferences

docker node update --label-add rack=1 --label-add datacenter=us-east <node-id>
docker node update --label-add rack=2 --label-add datacenter=us-west <node-id>

...........

sudo docker node update --label-add datacenter=dc1 --label-add rack=rack1 pc0

sudo docker node update --label-add datacenter=dc1 --label-add rack=rack2 pc1

sudo docker node update --label-add datacenter=dc1 --label-add rack=rack2 pc2

sudo docker node update --label-add datacenter=dc1 --label-add rack=rack3 pc3

sudo docker node update --label-add datacenter=dc1 --label-add rack=rack3 pc4

...........

mongo -u admin -p password --authenticationDatabase admin

use admin

db.getUser("admin")

use admin

db.updateUser("admin", { roles: [ { role: "root", db: "admin" } ] })

.............

db.createUser({user: 'admin', pwd: 'password', roles: [{role:"root", db:"admin"}]})

 var config = {     _id: "test-rs",     members: [         { _id: 0, host: "3b51fe37bab2:27017" },         { _id: 1, host: "81b2968a181c:27017" }, { _id: 2, host: "2afba2644b9d:27017" }     ] };

rs.reconfig(config, { force: true });
![image](https://github.com/SaraDanaKablTalabani/master_thesis/assets/101463904/4989aa79-6483-4944-846f-2e5b86865fda)

 
![image](https://github.com/SaraDanaKablTalabani/master_thesis/assets/101463904/6a541593-b777-4339-9832-c1e75a3cc3c5)

links:

1. https://github.com/smartsdk/mongo-rs-controller-swarm



