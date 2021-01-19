Launch container using following command to run eBPF program

sudo docker run --rm -it --privileged   -v /lib/modules:/lib/modules:ro   -v /sys:/sys:ro   -v /usr/src:/usr/src:ro <image id>
