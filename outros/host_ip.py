import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Computer Name: " + hostname)
print("IP Address: " + IPAddr)