sudo ip netns add server
sudo ip netns add client
sudo ip link add veth0 type veth peer name veth1
sudo ip link set veth0 netns server
sudo ip link set veth1 netns client
sudo ip netns exec server ip addr add 10.0.0.1/24 dev veth0
sudo ip netns exec client ip addr add 10.0.0.2/24 dev veth1
sudo ip netns exec server ip link set dev veth0 up
sudo ip netns exec client ip link set dev veth1 up
sudo ip netns exec server ip link set dev lo up
sudo ip netns exec client ip link set dev lo up
