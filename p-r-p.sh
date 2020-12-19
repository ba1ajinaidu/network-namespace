#creates 3 namespaces box1<--->router<---->box2
# box1 and box2 are connected by veth pairs 
sudo ip netns add box1
sudo ip netns add router
sudo ip netns add box2

sudo ip link add veth0 type veth peer name veth1
sudo ip link set veth0 netns box1
sudo ip link set veth1 netns router


sudo ip link add veth2 type veth peer name veth3
sudo ip link set veth2 netns box2
sudo ip link set veth3 netns router

sudo ip netns exec box1 ip addr add 10.0.0.2/24 dev veth0
sudo ip netns exec router  ip addr add 10.0.0.1/24 dev veth1

sudo ip netns exec box2 ip addr add 10.0.1.2/24 dev veth2
sudo ip netns exec router ip addr add 10.0.1.1/24 dev veth3

sudo ip netns exec box1 ip link set dev veth0 up
sudo ip netns exec router ip link set dev veth1 up
sudo ip netns exec box2 ip link set dev veth2 up
sudo ip netns exec router ip link set dev veth3 up


sudo echo 1 > /proc/sys/net/ipv4/ip_forward
sudo echo 1 > /proc/sys/net/netfilter/nf_log_all_netns

sudo ip netns exec box1 ip route add default via 10.0.0.1
sudo ip netns exec box2 ip route add default via 10.0.1.1
