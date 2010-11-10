import socket, fcntl, struct
import xmlrpclib

def get_ip_address(ifname="eth0"):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
    

def update_ip_hostname(admin_host="127.0.0.1", port=12000, hostname, ip_addr):
    admin_url = "http://" + admin_host + str(port)
    admin = xmlrpclib.ServerProxy(admin_url)
    try:
        admin.update_ip_hostname(hostname, ip_addr)
    except:
        pass

if __name__ == "__main__":
    print get_ip_address("lo")
    print get_ip_address()
    print get_ip_address("eth1")
