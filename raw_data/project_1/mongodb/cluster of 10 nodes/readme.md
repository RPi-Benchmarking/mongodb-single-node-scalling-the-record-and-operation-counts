sudo docker node update --label-add rack=1 pc0

sudo docker node update --label-add rack=2 pc1

sudo docker node update --label-add rack=3 pc2

sudo docker node update --label-add rack=4 pc3

sudo docker node update --label-add rack=5 pc4

sudo docker node update --label-add rack=6 pc20

sudo docker node update --label-add rack=7 pc21

sudo docker node update --label-add rack=8 pc22

sudo docker node update --label-add rack=9 pc23

sudo docker node update --label-add rack=10 pc24

...............

sudo docker node update --label-add rack=1 pc0

sudo docker node update --label-add rack=2 pc1

sudo docker node update --label-add rack=3 pc2

sudo docker node update --label-add rack=4 pc3

sudo docker node update --label-add rack=5 pc4

sudo docker node update --label-add rack=6 pc20

sudo docker node update --label-add rack=7 pc21

sudo docker node update --label-add rack=8 pc22

sudo docker node update --label-add rack=9 pc23

sudo docker node update --label-add rack=10 pc24

...................

labeling with group and rack

sudo docker node update --label-add group=1 pc0

sudo docker node update --label-add group=1 pc1

sudo docker node update --label-add group=1 pc2

sudo docker node update --label-add group=1 pc3

sudo docker node update --label-add group=1 pc4

sudo docker node update --label-add group=2 pc20

sudo docker node update --label-add group=2 pc21

sudo docker node update --label-add group=2 pc22

sudo docker node update --label-add group=2 pc23

sudo docker node update --label-add group=2 pc24

................

labeling the manger anfd the workers sepratly

# Label manager nodes (assuming pc0, pc1, and pc2 are managers)

sudo docker node update --label-add rack=1 pc0

sudo docker node update --label-add rack=2 pc1

sudo docker node update --label-add rack=3 pc2

# Label worker nodes (assuming pc3 to pc9 are workers)

sudo docker node update --label-add rack=4 pc3

sudo docker node update --label-add rack=5 pc4

sudo docker node update --label-add rack=6 pc5

sudo docker node update --label-add rack=7 pc6

sudo docker node update --label-add rack=8 pc7

sudo docker node update --label-add rack=9 pc8

sudo docker node update --label-add rack=10 pc9

.............

rs.add({ host: "52ee8fdbbea9:27017", priority: 0, votes: 0 })

 rs.add("dc199b4c25d7:27017")
 
.............

labeling of global and replica mode 9/9 and 9/10 respectively.

sudo docker node update --label-add role=manager pc0
sudo docker node update --label-add role=worker pc1
sudo docker node update --label-add role=worker pc2
sudo docker node update --label-add role=worker pc3
sudo docker node update --label-add role=worker pc4
sudo docker node update --label-add role=worker pc20
sudo docker node update --label-add role=worker pc21
sudo docker node update --label-add role=worker pc22
sudo docker node update --label-add role=worker pc23
sudo docker node update --label-add role=worker pc24


sudo docker node update --label-add datacenter=dc1 --label-add rack=rack1 pc0
sudo docker node update --label-add datacenter=dc1 --label-add rack=rack2 pc1
sudo docker node update --label-add datacenter=dc1 --label-add rack=rack2 pc2
sudo docker node update --label-add datacenter=dc1 --label-add rack=rack3 pc3
sudo docker node update --label-add datacenter=dc1 --label-add rack=rack3 pc4
sudo docker node update --label-add datacenter=dc2 --label-add rack=rack1 pc20
sudo docker node update --label-add datacenter=dc2 --label-add rack=rack2 pc21
sudo docker node update --label-add datacenter=dc2 --label-add rack=rack2 pc22
sudo docker node update --label-add datacenter=dc2 --label-add rack=rack3 pc23
sudo docker node update --label-add datacenter=dc2 --label-add rack=rack3 pc24



