#create namespaces
sudo ip netns add b1
sudo ip netns add b2
sudo ip netns add r1
sudo ip netns add r2

#create veth pairs and add them to the interfaces
sudo ip link add veth0 type veth peer name veth1
sudo ip link set veth0 netns b1
sudo ip link set veth1 netns r1


sudo ip link add veth2 type veth peer name veth3
sudo ip link set veth2 netns r1
sudo ip link set veth3 netns r2

sudo ip link add veth4 type veth peer name veth5
sudo ip link set veth4 netns r2
sudo ip link set veth5 netns b2

#assign ip addresses to the created veth pairs
sudo ip netns exec b1 ip addr add 10.0.0.2/24 dev veth0
sudo ip netns exec r1 ip addr add 10.0.0.1/24 dev veth1

sudo ip netns exec r1 ip addr add 10.0.1.1/24 dev veth2
sudo ip netns exec r2 ip addr add 10.0.1.2/24 dev veth3

sudo ip netns exec r2 ip addr add 10.1.1.1/24 dev veth4
sudo ip netns exec b2 ip addr add 10.1.1.2/24 dev veth5

#set the interfaces up
sudo ip netns exec b1 ip link set dev veth0 up
sudo ip netns exec r1 ip link set dev veth1 up
sudo ip netns exec r1 ip link set dev veth2 up
sudo ip netns exec r2 ip link set dev veth3 up
sudo ip netns exec r2 ip link set dev veth4 up
sudo ip netns exec b2 ip link set dev veth5 up

#enable ip forwarding
sudo ip netns exec r1 sysctl -w net.ipv4.conf.all.forwarding=1
sudo ip netns exec r2 sysctl -w net.ipv4.conf.all.forwarding=1

#add  route
sudo ip netns exec b1 ip route add default via 10.0.0.1
sudo ip netns exec b2 ip route add default via 10.1.1.1
sudo ip netns exec r1 ip route add default via 10.0.1.2
sudo ip netns exec r2 ip route add default via 10.0.1.1

