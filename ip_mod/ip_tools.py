import socket, fcntl, struct

def get_ip_address(ifname="eth0"):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

if __name__ == "__main__":
    print get_ip_address("lo")
    print get_ip_address()
    print get_ip_address("eth1")
